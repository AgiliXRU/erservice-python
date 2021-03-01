from emergency_response import EmergencyResponseService
from inbound import InboundPatientController
from vendor.pager_system import PagerSystem
from patient import Priority


class AlertScanner:
    ADMIN_ON_CALL_DEVICE = "111-111-1111"

    manager: EmergencyResponseService
    controller: InboundPatientController
    critical_patient_notifications_sent = list()

    def __init__(self, staff_assignment_manager, inbound_patient_controller):
        self.manager = staff_assignment_manager
        self.controller = inbound_patient_controller

    def scan(self):
        print("Scanning for situations requiring alerting...")
        inbound = self.controller.current_inbound_patients()
        for patient in inbound:
            if patient.get_priority() == Priority.RED:
                if patient.get_transport_id() not in self.critical_patient_notifications_sent:
                    self.alert_for_new_critical_patient(patient)
            if patient.get_priority() == Priority.YELLOW and patient.get_condition() == "heart arrhythmia":
                if patient.get_transport_id() not in self.critical_patient_notifications_sent:
                    self.alert_for_new_critical_patient(patient)

    def alert_for_new_critical_patient(self, patient):
        try:
            if patient.get_priority() == Priority.RED:
                self.transmit_with_acknowledge(self.ADMIN_ON_CALL_DEVICE,
                                               "New inbound critical patient: " + str(patient.get_transport_id()))
            if patient.get_priority() == Priority.YELLOW:
                self.transmit(self.ADMIN_ON_CALL_DEVICE,
                              "New inbound critical patient: " + str(patient.get_transport_id()))

            self.critical_patient_notifications_sent.append(patient.get_transport_id())
        except RuntimeError:
            print("Failed attempt to use pager system to device " + self.ADMIN_ON_CALL_DEVICE)

    def transmit_with_acknowledge(self, device, text):
        transport = PagerSystem.get_transport()
        transport.initialize()
        transport.transmit_requiring_acknowledgement(device, text)

    def transmit(self, device, text):
        transport = PagerSystem.get_transport()
        transport.initialize()
        transport.transmit(device, text)

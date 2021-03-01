from inbound import InboundPatientController
from assignment import StaffAssignmentManager


class AssignPatientToBedCommand(object):
    staff_manager: StaffAssignmentManager
    inbound_patient_controller: InboundPatientController

    def __init__(self, manager, inbound_patient_controller):
        self.staff_manager = manager
        self.inbound_patient_controller = inbound_patient_controller

    def assign_patient_to_bed(self, transport_id, bed_id):
        bed = self.staff_manager.get_bed_by_id(bed_id)
        patient = self.get_patient_by_transport(transport_id)
        self.staff_manager.assign_patient_to_bed(patient, bed)
        self.inbound_patient_controller.inform_of_patient_arrival(transport_id)

    def get_patient_by_transport(self, transport_id):
        for patient in self.inbound_patient_controller.current_inbound_patients():
            if patient.transport_id == transport_id:
                return patient
        raise RuntimeError("Unable to find inbound patient " + transport_id)
from xml.etree import ElementTree

from emergency_response import EmergencyResponseService
from patient import Patient, Priority


class InboundPatientController(object):
    transport_service: EmergencyResponseService

    def __init__(self, transport_service):
        self.transport_service = transport_service

    def current_inbound_patients(self):
        xml_for_inbound = self.transport_service.fetch_inbound_patients()
        patients = list()
        try:
            print("Recieved XML from transport service: {}\n".format(xml_for_inbound))
            root = ElementTree.fromstring(xml_for_inbound)
            for node in root:
                patient = Patient()
                for subnode in node:
                    if subnode.tag == 'Name':
                        patient.set_name(subnode.text)
                    if subnode.tag == 'TransportId':
                        patient.set_transport_id(int(subnode.text))
                    if subnode.tag == 'Priority':
                        patient.set_priority(Priority[subnode.text])
                patients.append(patient)
        except RuntimeError as e:
            print(str(e))
        print("Returning inbound patients: " + str(len(patients)))
        return patients

    def inform_of_patient_arrival(self, transport_id):
        self.transport_service.inform_of_arrival(transport_id)

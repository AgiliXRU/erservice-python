from inbound import InboundPatientController
from patient import Priority, Patient
from scanner import AlertScanner


class StubInboundPatientController(InboundPatientController):

    def __init__(self, patients):
        self.patients = patients

    def current_inbound_patients(self):
        return self.patients


def create_patient(transport_id, priority, condition=""):
    patient = Patient()
    patient.set_transport_id(transport_id)
    patient.set_priority(priority)
    patient.set_condition(condition)
    return patient


class MockAlertScanner(AlertScanner):
    acknowledged = list()
    regular = list()

    def transmit_with_acknowledge(self, device, text):
        self.acknowledged.append(text)

    def transmit(self, device, text):
        self.regular.append(text)


def test_scan_for_red_priority_patients():
    patients = list()
    patients.append(create_patient(11, Priority.RED))
    patients.append(create_patient(12, Priority.YELLOW, "heart arrhythmia"))
    scanner = MockAlertScanner(None, StubInboundPatientController(patients))

    scanner.scan()

    assert len(scanner.acknowledged) == 1
    assert scanner.acknowledged[0] == "New inbound critical patient: 11"
    assert len(scanner.regular) == 1
    assert scanner.regular[0] == "New inbound critical patient: 12"

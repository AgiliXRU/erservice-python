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

    patients = list()

    def alert_for_new_critical_patient(self, patient):
        self.patients.append(patient)


def test_scan_for_red_priority_patients():
    patients = list()
    patients.append(create_patient(11, Priority.RED))
    patients.append(create_patient(12, Priority.YELLOW, "heart arrhythmia"))
    scanner = MockAlertScanner(None, StubInboundPatientController(patients))

    scanner.scan()

    assert len(scanner.patients) == 2
    assert scanner.patients[0].get_transport_id() == 11
    assert scanner.patients[0].get_priority() == Priority.RED
    assert scanner.patients[1].get_transport_id() == 12
    assert scanner.patients[1].get_priority() == Priority.YELLOW
    assert scanner.patients[1].get_condition() == "heart arrhythmia"

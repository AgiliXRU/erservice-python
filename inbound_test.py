from inbound import InboundPatientController
from patient import Priority


def test_current_inbound_patients():
    controller = InboundPatientController(None)
    xml = "<Inbound>" \
          "<Patient>" \
          "<TransportId>1</TransportId>" \
          "<Name>John Doe</Name>" \
          "<Condition>heart arrhythmia</Condition>" \
          "<Priority>YELLOW</Priority>" \
          "<Birthdate></Birthdate>" \
          "</Patient>" \
          "</Inbound>"
    patients = controller.get_patients_from_xml(xml)

    assert len(patients) == 1
    assert patients[0].get_name() == "John Doe"
    assert patients[0].get_transport_id() == 1
    assert patients[0].get_priority() == Priority.YELLOW
    assert patients[0].get_condition() == "heart arrhythmia"


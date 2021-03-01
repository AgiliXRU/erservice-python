from divergence import DivergenceController, DivergenceReport
from patient import Patient


def create_patient(condition):
    patient = Patient()
    patient.set_condition(condition)
    return patient


def test_affected_patients():
    controller = DivergenceController()

    patients = list()
    patients.append(create_patient("ambulatory"))
    patients.append(create_patient("stroke"))

    result = controller.affected_patients(patients)

    assert len(result) == 1


def test_report_generation():
    report = DivergenceReport(1, 2, 3)

    text = report.generate()

    assert text == "Situation report\n" \
                   "Inbound patients requiring beds: 1 Red, 2 Yellow, 3 Green."

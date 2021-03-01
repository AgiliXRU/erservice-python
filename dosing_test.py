from datetime import date

import pytest
from dateutil.relativedelta import relativedelta

from patient import Patient
from dosing import DosingCalculator

patient = Patient()
dosing_calculator = DosingCalculator()


def test_returns_correct_doses_for_neonate():
    patient.set_birthdate(date.today() - relativedelta(months=1))

    single_dose = dosing_calculator.get_recommended_single_dose(patient, "Tylenol Oral Suspension")

    assert single_dose == "0"


def test_returns_correct_doses_for_infant():
    patient.set_birthdate(date.today() - relativedelta(days=40))

    single_dose = dosing_calculator.get_recommended_single_dose(patient, "Tylenol Oral Suspension")

    assert single_dose == "2.5 ml"


def test_returns_correct_doses_for_child():
    patient.set_birthdate(date.today() - relativedelta(years=3))

    single_dose = dosing_calculator.get_recommended_single_dose(patient, "Tylenol Oral Suspension")

    assert single_dose == "5 ml"


def test_returns_correct_doses_for_neonate_amox():
    patient.set_birthdate(date.today() - relativedelta(days=20))

    single_dose = dosing_calculator.get_recommended_single_dose(patient, "Amoxicillin Oral Suspension")
    assert single_dose == "15 mg/kg"


def test_raises_exception_for_adults():
    patient.set_birthdate(date.today() - relativedelta(years=16))

    with pytest.raises(RuntimeError):
        dosing_calculator.get_recommended_single_dose(patient, "Amoxicillin Oral Suspension")


def test_null_for_unrecognized_medication():
    patient.set_birthdate(date.today() - relativedelta(years=16))
    with pytest.raises(RuntimeError):
        dosing_calculator.get_recommended_single_dose(patient,"No Such Med")

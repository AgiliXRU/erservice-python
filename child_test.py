from child import ChildClassification, calculate
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

current_date = date.today()


def test_return_neonate_up_to_30_days_old():
    assert calculate(current_date, current_date) == ChildClassification.NEONATE

    birth_date = current_date - timedelta(days=30)
    assert calculate(birth_date, current_date)


def test_return_infant_from_30_days_to_2_years():
    birth_date = current_date - relativedelta(days=30)
    assert calculate(birth_date, current_date) == ChildClassification.INFANT

    birth_date = current_date - relativedelta(years=2) + relativedelta(days=1)
    assert calculate(birth_date, current_date) == ChildClassification.INFANT


def test_return_child_from_2_years_to_12_years():
    birth_date = current_date - relativedelta(years=2)
    assert calculate(birth_date, current_date) == ChildClassification.CHILD

    birth_date = current_date - relativedelta(years=12) + relativedelta(days=1)
    assert calculate(birth_date, current_date) == ChildClassification.CHILD


def test_return_adolescent_from_12_years_to_16_years():
    birth_date = current_date - relativedelta(years=12)
    assert calculate(birth_date, current_date) == ChildClassification.ADOLESCENT

    birth_date = current_date - relativedelta(years=16) + relativedelta(days=1)
    assert calculate(birth_date, current_date) == ChildClassification.ADOLESCENT


def test_return_undefined_after_16_years():
    birth_date = current_date - relativedelta(years=16)
    assert calculate(birth_date, current_date) == ChildClassification.UNDEFINED

    birth_date = current_date - relativedelta(years=80)
    assert calculate(birth_date, current_date) == ChildClassification.UNDEFINED


def test_return_undefined_if_birthdate_in_future():
    birth_date = current_date + relativedelta(days=1)
    assert calculate(birth_date, current_date) == ChildClassification.UNDEFINED

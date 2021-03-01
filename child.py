from enum import Enum

from dateutil.relativedelta import relativedelta


class ChildDosingDatabase:
    doses = dict()

    def __init__(self):
        self.init_dose("Tylenol Oral Suspension", ChildClassification.NEONATE, "0")
        self.init_dose("Tylenol Oral Suspension", ChildClassification.INFANT, "2.5 ml");
        self.init_dose("Tylenol Oral Suspension", ChildClassification.CHILD, "5 ml");
        self.init_dose("Tylenol Oral Suspension", ChildClassification.ADOLESCENT, "15 ml");
        self.init_dose("Amoxicillin Oral Suspension", ChildClassification.NEONATE, "15 mg/kg");
        self.init_dose("Amoxicillin Oral Suspension", ChildClassification.INFANT, "50 mg/kg");
        self.init_dose("Amoxicillin Oral Suspension", ChildClassification.CHILD, "80 mg/kg");
        self.init_dose("Amoxicillin Oral Suspension", ChildClassification.ADOLESCENT, "120 mg/kg");

    def init_dose(self, medication, classification, dose):
        self.doses[medication + classification.name] = dose

    def get_single_dose(self, medication, classification):
        if classification == ChildClassification.UNDEFINED:
            raise RuntimeError("Disallowed dosing lookup for " + medication + ", " + classification.name)
        return self.doses[medication + classification.name]


def calculate(birth_date, current_date):
    days_old = (current_date - birth_date).days
    years_old = relativedelta(current_date, birth_date).years

    if 0 <= days_old < 30:
        return ChildClassification.NEONATE

    if days_old >= 30 and years_old < 2:
        return ChildClassification.INFANT

    if 2 <= years_old < 12:
        return ChildClassification.CHILD

    if 12 <= years_old < 16:
        return ChildClassification.ADOLESCENT

    if years_old >= 16:
        return ChildClassification.UNDEFINED

    return ChildClassification.UNDEFINED


class ChildClassification(Enum):
    NEONATE = 1
    INFANT = 2
    CHILD = 3
    ADOLESCENT = 4
    UNDEFINED = 5

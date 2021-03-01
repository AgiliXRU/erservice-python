from patient import Patient


class Bed(object):
    bed_id: int
    critical_care: bool
    patient_assigned: Patient

    def __init__(self, bed_id, critical_care):
        self.bed_id = bed_id
        self.critical_care = critical_care

    def assign_patient(self, patient):
        self.patient_assigned = patient

    def patient_discharged(self):
        self.patient_assigned = None

    def get_patient_assigned(self):
        self.patient_assigned

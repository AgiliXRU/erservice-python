from child import ChildClassification, ChildDosingDatabase


class DosingCalculator:

    def get_recommended_single_dose(self, patient,  medication):
        dosing_source = DosingSourceFactory.get_dosing_source_for(patient, medication)
        return dosing_source.get_single_dose(medication, patient.get_child_classification())


class DosingSourceFactory(object):
    @classmethod
    def get_dosing_source_for(cls, patient, medication):
        if ChildClassification.UNDEFINED != patient.get_child_classification():
            return ChildDosingDatabase()
        raise RuntimeError("Dosing Calculator to use for patient and medication undefined")
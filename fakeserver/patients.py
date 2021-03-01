from patient import Patient


class PatientsToXML(object):
    patients_in_transport = list()

    def __init__(self, patients_in_transport):
        self.patients_in_transport = patients_in_transport
        self.transport_ids = 1
        patient = Patient()
        patient.set_name("John Doe")
        patient.set_priority("YELLOW")
        patient.set_transport_id(self.transport_ids)
        self.patients_in_transport.append(patient)
        self.transport_ids += 1

    def patients_to_xml(self):
        xml = "<Inbound>\n"
        for patient in self.patients_in_transport:
            xml += "\t<Patient>\n"
            xml += "\t\t<TransportId>" + str(patient.get_transport_id()) + "</TransportId>\n"
            xml += "\t\t<Name>" + patient.get_name() + "</Name>\n"
            xml += "\t\t<Condition>heart arrhythmia</Condition>\n"
            xml += "\t\t<Priority>" + patient.get_priority() + "</Priority>\n"
            xml += "\t\t<Birthdate>"
            if patient.get_birthdate() is not None:
                xml += patient.get_birthdate()
            xml += "</Birthdate>\n"
            xml += "\t</Patient>\n"
        xml += "</Inbound>"
        return xml

    def remove_inbound(self, transport_id):
        arrived = None
        for patient in self.patients_in_transport:
            if transport_id == patient.get_transport_id():
                arrived = patient
        if arrived is not None:
            self.patients_in_transport.remove(arrived)

    def add_inbound(self, patient):
        patient.set_transport_id(self.transport_ids)
        self.transport_ids += 1
        self.patients_in_transport.append(patient)

    def stop_diversion(self, priority):
        patients_to_divert = list()
        for patient in patients_to_divert:
            if patient.get_priority() == priority:
                patients_to_divert.append(patient)
        for patient in patients_to_divert:
            self.patients_in_transport.remove(patient)

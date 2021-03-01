import requests


class EmergencyResponseService:
    connection_string: str
    timeout: int

    def __init__(self, url, port, timeout):
        self.connection_string = "http://" + url + ":" + str(port)
        self.timeout = timeout
        acknowledge = False
        print("Initializing with Emergency Response Services: " + self.connection_string + "/ack")
        try:
            response = requests.post(self.connection_string + "/ack", "ER system ping").text
        except IOError as e:
            raise RuntimeError("Unable to connect with Emergency Respose Services")
        print(response)
        if response != "acknowledged":
            raise RuntimeError("Unable to connect with Emergency Respose Services");

    def fetch_inbound_patients(self):
        try:
            response = requests.get(self.connection_string + "/inbound", timeout=self.timeout).text
        except IOError as e:
            raise RuntimeError("Unable to obtain inbound patients: " + str(e))

        return response

    def inform_of_arrival(self, transport_id):
        try:
            response = requests.post(
                self.connection_string + "/arrived" + "?transportId=" + transport_id,
                timeout=self.timeout
            ).text
        except IOError as e:
            print(e)
            raise RuntimeError("Unable to inform of arrival: " + e)

        if response != "OK":
            raise RuntimeError("Unable to inform of arrival")

    def request_inbound_diversion(self, priority):
        try:
            response = requests.post(
                self.connection_string + "/diversion" + "?priority=" + priority.name()
            ).text
        except IOError as e:
            raise RuntimeError("Unable to inform of diversion")

        if "OK" != response:
            raise RuntimeError("Unable to inform of diversion")

    def remove_inbound_diversion(self, priority):
        try:
            response = requests.post(self.connection_string + "/diversionStop" + "?priority=" + priority.name()).text
        except IOError as e:
            raise RuntimeError("Unable to remove diversion", e)

        if "OK" != response:
            raise RuntimeError("Unable to remove diversion")

from datetime import date
from enum import Enum
from json import JSONEncoder

from child import calculate


class Priority(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2
    BLACK = 3


class Patient:
    name: str
    birthdate = None
    priority: Priority
    transport_id: int
    condition: str

    def get_name(self):
        return self.name

    def get_birthdate(self):
        return self.birthdate

    def get_priority(self):
        return self.priority

    def get_transport_id(self):
        return self.transport_id

    def get_condition(self):
        return self.condition

    def set_name(self, name):
        self.name = name

    def set_transport_id(self, transport_id):
        self.transport_id = transport_id

    def set_priority(self, priority):
        self.priority = priority

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_condition(self, condition):
        self.condition = condition

    def get_child_classification(self):
        return calculate(self.birthdate, date.today())


class PatientEncoder(JSONEncoder):
    def default(self, o):
        return {
            "transportId": int(o.transport_id),
            "name": o.name,
            "priority": o.priority
        }

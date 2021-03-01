from enum import Enum
from json import JSONEncoder


class Staff:
    staff_id = None
    name = None
    role = None

    def __init__(self, staff_id, name, role):
        self.staff_id = staff_id
        self.name = name
        self.role = role


class StaffEncoder(JSONEncoder):
    def default(self, o):
        return {
            "staffId": o.staff_id,
            "name": o.name,
            "role": o.role.name
        }


class StaffRole(Enum):
    DOCTOR = 1
    RESIDENT = 2
    NURSE = 3

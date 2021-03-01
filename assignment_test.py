from assignment import StaffAssignmentManager
from repository.beds import BedRepository
from repository.staff import StaffRepository
from staff import Staff, StaffRole


class StubStaffRepository(StaffRepository):
    staff = list()

    def __init__(self, list):
        self.staff = list

    def get_shift_staff(self):
        return self.staff


class StubBedRepository(BedRepository):

    def get_all_beds(self):
        return list()


def create_staff(id, name, role):
    return Staff(id, name, role)


def test_get_physicians_on_duty_should_return_list_of_doctors():
    staff = list()
    staff.append(create_staff(1, "Don Doctor", StaffRole.DOCTOR))
    staff.append(create_staff(2, "Ron Resident", StaffRole.RESIDENT))
    staff.append(create_staff(3, "Nancy Resident", StaffRole.NURSE))
    manager = StaffAssignmentManager(StubStaffRepository(staff), StubBedRepository())

    staff = manager.get_physicians_on_duty()

    assert len(staff) == 2
    assert staff[0].role == StaffRole.DOCTOR
    assert staff[1].role == StaffRole.RESIDENT

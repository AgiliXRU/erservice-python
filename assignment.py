from repository.beds import BedRepository
from repository.staff import StaffRepository
from staff import StaffRole


def assign_patient_to_bed(patient, bed):
    bed.assign_patient(patient)


class StaffAssignmentManager:
    shift_staff = list()
    beds = list()
    bed_staff_assignments = dict()

    def __init__(self):
        staff_repo = StaffRepository()
        self.shift_staff = staff_repo.get_shift_staff()
        bed_repo = BedRepository()
        self.beds = bed_repo.get_all_beds()

    def get_shift_staff(self):
        return self.shift_staff

    def get_available_staff(self):
        available_staff = list()
        for staff in self.shift_staff:
            staff_assigned = False
            for bed_list in self.bed_staff_assignments:
                if bed_list in staff:
                    staff_assigned = True
            if not staff_assigned:
                available_staff.append(staff)

        return available_staff

    def get_physicians_on_duty(self):
        physicians = list()
        for staff in self.shift_staff:
            if staff.role == StaffRole.DOCTOR:
                physicians.append(staff)
        return physicians

    def get_bed_by_id(self, bed_id):
        for bed in self.beds:
            if bed.bed_id == bed_id:
                return bed
        return None

    def get_staff_by_id(self, staff_id):
        for staff in self.shift_staff:
            if staff.staff_id == staff_id:
                return staff
        return None

    def assign_staff_member_to_bed(self, staff, bed):
        currently_assigned_to_bed = self.bed_staff_assignments[bed]
        if len(currently_assigned_to_bed) == 0:
            currently_assigned_to_bed = list()
        currently_assigned_to_bed.append(staff)
        self.bed_staff_assignments[bed] = currently_assigned_to_bed

    def get_beds(self):
        return self.beds

    def get_available_beds(self):
        available_beds = list()
        for bed in self.beds:
            if bed.get_patient_assigned() is None:
                available_beds.append(bed)
        return available_beds

    



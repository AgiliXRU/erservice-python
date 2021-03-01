from assignment import StaffAssignmentManager


class AssignStaffToBedCommand(object):
    staff_manager: StaffAssignmentManager

    def __init__(self, manager):
        self.staff_manager = manager

    def assign_staff_to_bed(self, staff_ids, bed_id):
        for staff_id in staff_ids:
            staff = self.staff_manager.get_staff_by_id(staff_id)
            bed = self.staff_manager.get_bed_by_id(bed_id)
            self.staff_manager.assign_staff_member_to_bed(staff, bed)


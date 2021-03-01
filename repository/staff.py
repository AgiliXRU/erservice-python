from staff import Staff, StaffRole


class StaffRepository(object):
    staff_file = "data/staff.csv"
    f = None

    def __init__(self):
        try:
            self.f = open(self.staff_file, "r")
        except IOError as e:
            print(e)
            RuntimeError(e)

    def get_shift_staff(self):
        staff_list = list()
        for l in self.f:
            values = l.rstrip().split(",")
            emp_id = int(values[0])
            name = values[1]
            role = values[2]
            staff = Staff(emp_id, name, StaffRole[role])
            staff_list.append(staff)
        return staff_list

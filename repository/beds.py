from bed import Bed


class BedRepository(object):
    staff_file = "data/beds.csv"
    f = None

    def __init__(self):
        try:
            self.f = open(self.staff_file, "r")
        except IOError as e:
            print(e)

    def get_all_beds(self):
        beds_list = list()
        for l in self.f:
            values = l.rstrip().split(",")
            bed_id = int(values[0])
            if values[1] == 'true':
                equipped_crit = True
            else:
                equipped_crit = False
            bed = Bed(bed_id, equipped_crit)
            beds_list.append(bed)
        return beds_list


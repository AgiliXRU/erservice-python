from emergency_response import EmergencyResponseService
from patient import Priority
from staff import StaffRole
from inbound import InboundPatientController
from assignment import StaffAssignmentManager
from vendor.pager_system import PagerSystem


class DivergenceController:
    ADMIN_ON_CALL_DEVICE = "111-111-1111"

    red_divergence: bool
    yellow_divergence: bool
    green_divergence: bool
    red_count: int
    yellow_count: int
    green_count: int
    allowed_count: int
    red_over: int
    yellow_over: int
    green_over: int

    def __init__(self):
        self.red_divergence = False
        self.yellow_divergence = False
        self.green_divergence = False
        self.red_count = 0
        self.yellow_count = 0
        self.green_count = 0
        self.allowed_count = 3
        self.red_over = 0
        self.yellow_over = 1
        self.green_over = 4

    def check(self):
        manager = StaffAssignmentManager()
        transport_service = EmergencyResponseService("http://localhost", 4567, 1000)
        controller = InboundPatientController(transport_service)
        red = [1, 2]
        yellow = [1, 1]
        green = [0, 1]
        red_incremented = False
        yellow_incremented = False
        green_incremented = False
        patients = controller.current_inbound_patients()
        staff = manager.get_available_staff()
        beds = manager.get_available_beds()
        bedcrits = 0
        redin = 0
        yellowin = 0
        greenin = 0
        staffcur = [0, 0]
        need = [0, 0]

        for bed in beds:
            if bed.is_critical_care():
                bedcrits += 1

        for patient in self.affected_patients(patients):
            if patient.get_priority() == Priority.RED:
                redin += 1
            elif patient.getPriority() == Priority.YELLOW:
                yellowin += 1
            elif patient.getPriority() == Priority.GREEN:
                greenin += 1

        for cur in staff:
            if cur.get_role() == StaffRole.DOCTOR:
                staffcur[0] += 1
            elif StaffRole.NURSE == cur.getRole():
                staffcur[1] += 1

        if redin > (bedcrits + self.red_over):
            self.red_count += 1
            red_incremented = True

        if yellowin + greenin > (beds.size() - bedcrits + self.yellow_over + self.green_over):
            if greenin > (beds.size() - bedcrits + self.green_over) and yellowin <= (
                    beds.size() - bedcrits + self.yellow_over):
                self.green_count += 1
                green_incremented = True
            else:
                self.green_count += 1
                self.yellow_count += 1
                green_incremented = True
                yellow_incremented = True

        need[0] = redin * red[0]
        need[0] += yellowin * yellow[0]
        need[0] += greenin * green[0]
        need[1] = redin * red[1]
        need[1] += yellowin * yellow[1]
        need[1] += greenin * green[1]

        if need[0] > staffcur[0]:
            diff = need[0] - staffcur[0]
            if greenin * green[0] >= diff:
                if not green_incremented:
                    green_incremented = True
                    self.green_count += 1
            else:
                both = (yellowin * yellow[0]) + (greenin * green[0])
                if both >= diff:
                    if not green_incremented:
                        green_incremented = True
                        self.green_count += 1
                    if not yellow_incremented:
                        yellow_incremented = True
                        self.yellow_count += 1
                else:
                    if not green_incremented:
                        green_incremented = True
                        self.green_count += 1
                    if not yellow_incremented:
                        yellow_incremented = True
                        self.yellow_count += 1

                    if not red_incremented:
                        red_incremented = True
                        self.red_count += 1

        if need[1] > staffcur[1]:
            diff = need[1] - staffcur[1]
            if (greenin * green[1]) >= diff:
                if not green_incremented:
                    green_incremented = True
                    self.green_count += 1
            else:
                both = (yellowin * yellow[1]) + (greenin * green[1])
                if both >= diff:
                    if not green_incremented:
                        green_incremented = True
                        self.green_count += 1

                    if not yellow_incremented:
                        yellow_incremented = True
                        self.yellow_count += 1
                else:
                    if not green_incremented:
                        green_incremented = True
                        self.green_count += 1

                    if not yellow_incremented:
                        yellow_incremented = True
                        self.yellow_count += 1

                    if not red_incremented:
                        red_incremented = True
                        self.red_count += 1

        if red_incremented:
            if self.red_count > self.allowed_count and not self.red_divergence:
                self.red_divergence = True
                transport_service.request_inbound_diversion(Priority.RED)
                self.send_divergence_page("Entered divergence for RED priority patients!", True)
                self.red_count = 0
        else:
            self.red_count = 0
            if self.red_divergence:
                transport_service.remove_inbound_diversion(Priority.RED)
                self.send_divergence_page("Ended divergence for RED priority patients.", True)
                self.red_divergence = False
        if yellow_incremented:
            if self.yellow_count > self.allowed_count and not self.yellow_divergence:
                self.yellow_divergence = True
                transport_service.request_inbound_diversion(Priority.YELLOW)
                self.send_divergence_page("Entered divergence for YELLOW priority patients!", True)
                self.yellow_count = 0

        else:
            self.yellow_count = 0
            if self.yellow_divergence:
                transport_service.remove_inbound_diversion(Priority.YELLOW)
                self.send_divergence_page("Ended divergence for YELLOW priority patients.", False)
                self.yellow_divergence = False
        if green_incremented:
            if self.green_count > self.allowed_count and not self.green_divergence:
                self.green_divergence = True
                transport_service.request_inbound_diversion(Priority.GREEN)
                self.send_divergence_page("Entered divergence for GREEN priority patients!", True)
                self.green_count = 0

        else:
            self.green_count = 0
            if self.green_divergence:
                transport_service.remove_inbound_diversion(Priority.GREEN)
                self.send_divergence_page("Ended divergence for GREEN priority patients.", False)
                self.green_divergence = False

    def send_divergence_page(self, text, require_ack):
        try:
            transport = PagerSystem.get_transport()
            transport.initialize()
            if require_ack:
                transport.transmitRequiringAcknowledgement(self.ADMIN_ON_CALL_DEVICE, text)
            else:
                transport.transmit(self.ADMIN_ON_CALL_DEVICE, text)

        except RuntimeError as e:
            print(e)

    def affected_patients(self, patients):
        result = list()
        for patient in patients:
            if "ambulatory" not in patient.get_condition():
                result.append(patient)
        return result

import json
import falcon

from assign_patient import AssignPatientToBedCommand
from assign_staff import AssignStaffToBedCommand
from emergency_response import EmergencyResponseService
from staff import StaffEncoder
from assignment import StaffAssignmentManager
from scanner import AlertScanner
from inbound import InboundPatientController
from patient import PatientEncoder


class CurrentInboundPatients:

    def on_get(self, req, resp):
        print("Recieved request for inbound patients from client.")
        controller = InboundPatientController(EmergencyResponseService("localhost", 4567, 1000))
        patients = controller.current_inbound_patients()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(patients, cls=PatientEncoder, indent=4)


class ScanForCritical(object):

    def on_get(self, req, resp):
        AlertScanner(StaffAssignmentManager(),
                     InboundPatientController(EmergencyResponseService("localhost", 4567, 1000))).scan()
        resp.status = falcon.HTTP_200
        resp.body = "OK"


class PhysiciansOnDuty(object):
    manager: StaffAssignmentManager

    def __init__(self):
        self.manager = StaffAssignmentManager()

    def on_get(self, req, resp):
        print("Recieved request for physicians on duty from client.")
        physicians = self.manager.get_physicians_on_duty()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(physicians, cls=StaffEncoder, indent=4)


class ShiftStaff(object):

    def __init__(self):
        self.manager = StaffAssignmentManager()

    def on_get(self, req, resp):
        print("Recieved request for all shift staff from client.")
        physicians = self.manager.get_shift_staff()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(physicians, cls=StaffEncoder, indent=4)


class AvailableStaff(object):
    def __init__(self):
        self.manager = StaffAssignmentManager()

    def on_get(self, req, resp):
        print("Recieved request for available staff from client.")
        physicians = self.manager.get_available_staff()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(physicians, cls=StaffEncoder, indent=4)


class Beds(object):
    def __init__(self):
        self.manager = StaffAssignmentManager()

    def on_get(self, req, resp):
        print("Recieved request for all beds from client.")
        physicians = self.manager.get_beds()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(physicians, cls=StaffEncoder, indent=4)


class AssignToBed(object):
    emergency_transport_service: EmergencyResponseService


class AvailableBeds(object):
    def __init__(self):
        self.manager = StaffAssignmentManager()

    def on_get(self, req, resp):
        print("Recieved request for available beds from client.")
        physicians = self.manager.get_available_beds()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(physicians, cls=StaffEncoder, indent=4)


class AssignPatientToBed(AssignToBed):
    def on_post(self, req, resp):
        transport_id = int(req.queryParams("transportId"))
        bed_id = int(req.queryParams("bedId"))
        print(f"Client request to assign patient {transport_id} to bed {bed_id}")
        command = AssignPatientToBedCommand(StaffAssignmentManager(),
                                            InboundPatientController(self.emergency_transport_service))
        command.assign_patient_to_bed(transport_id, bed_id)
        resp.status = falcon.HTTP_200
        resp.body = "OK"


class AssignStaffToBed(AssignToBed):

    def on_post(self, req, resp):
        transport_id = int(req.queryParams("transportId"))
        bed_id = int(req.queryParams("bedId"))
        print(f"Client request to assign patient {transport_id} to bed {bed_id}")
        command = AssignStaffToBedCommand(StaffAssignmentManager())
        command.assign_staff_to_bed(transport_id, bed_id)
        resp.status = falcon.HTTP_200
        resp.body = "OK"


class EREndpoints:

    def initialize_endpoints(self, app):
        app.add_route('/inboundPatients', CurrentInboundPatients())
        app.add_route('/shiftStaff', ShiftStaff())
        app.add_route('/availableStaff', AvailableStaff())
        app.add_route('/physiciansOnDuty', PhysiciansOnDuty())
        app.add_route('/beds', Beds())
        app.add_route('/availableBeds', AvailableBeds())
        app.add_route('/assignPatientToBed', AssignPatientToBed())
        app.add_route('/assignStaffToBed', AssignStaffToBed())
        app.add_route('/scanForCritical', ScanForCritical())

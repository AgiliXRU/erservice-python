import falcon

from fakeserver.patients import PatientsToXML
from patient import Patient, Priority


class AckResponse(object):
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "acknowledged"


class CheckResponse(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "OK"


class Arrived(object):

    def on_post(self, req, resp):
        transport_id = int(req.params["transportId"])
        xml.remove_inbound(transport_id)
        resp.status = falcon.HTTP_200
        resp.body = "OK"


class Inbound(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = xml.patients_to_xml()


class SimulateNewTransport(object):

    def on_post(self, req, resp):

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body. A valid JSON document is required.')
        try:
            req.context.doc = falcon.json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753, 'Malformed JSON')

        patient = Patient()
        patient.set_name(req.context.doc['name'])
        patient.set_priority(req.context.doc['priority'])
        xml.add_inbound(patient)

        resp.status = falcon.HTTP_200
        resp.body = "OK"


class Diversion(object):
    def on_post(self, req, resp):
        print(req.params["priority"])
        priority = Priority[req.params["priority"]]
        resp.status = falcon.HTTP_200
        resp.body = "OK"


class DiversionStop(object):
    def on_post(self, req, resp):
        priority = Priority[req.params["priority"]]
        print(f"Transport service diverting patients with priority {priority}")
        xml.stop_diversion(priority)
        resp.status = falcon.HTTP_200
        resp.body = "OK"


xml = PatientsToXML(list())
app = falcon.App()
app.add_route('/ack', AckResponse())
app.add_route('/check', CheckResponse())
app.add_route('/inbound', Inbound())
app.add_route('/simulateNewTransport', SimulateNewTransport())
app.add_route('/diversion', Diversion())
app.add_route('/arrived', Arrived())
app.add_route('/diversionStop', DiversionStop())

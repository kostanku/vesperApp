
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from profile import Profile
from vesperapp import VesperApp


app = Flask(__name__)
vp = VesperApp()
CORS(app)


@app.route('/', methods=['GET'])
def get_ui():
    return send_from_directory('ui', 'cvjm_vesper.html')


@app.route('/appointments', methods=['GET'])
def get_all_appointments():
    all_appointments = vp.get_all_appointments()
    jsonable_aptmts = [aptmt.__dict__ for aptmt in all_appointments]
    return jsonify(jsonable_aptmts), 500


@app.route('/appointments/host', methods=['GET'])
def get_host_appointments():
    values = request.args
    id = values['id']
    print(id)
    all_appointments = vp.get_host_appointments(id)
    jsonable_aptmts = [aptmt.__dict__ for aptmt in all_appointments]
    return jsonify(jsonable_aptmts), 500


@app.route('/appointments/guest', methods=['GET'])
def get_guest_appointments():
    values = request.args
    id = values['id']
    print(id)
    all_appointments = vp.get_guest_appointments(id)
    jsonable_aptmts = [aptmt.__dict__ for aptmt in all_appointments]
    print(jsonable_aptmts)
    return jsonify(jsonable_aptmts), 500


@app.route('/appointment', methods=['DELETE'])
def delete_appointment():
    values = request.args
    id = values['id']
    print(id)
    all_appointments = vp.get_all_appointments()
    new_all_appointments = [[aptmt for aptmt
                             in all_appointments if aptmt.id != id]]
    vp.all_appointments = new_all_appointments
    aptmts = [aptmt.__dict__ for aptmt in new_all_appointments]
    print(aptmts)
    return jsonify(aptmts), 500


@app.route('/appointment', methods=['POST'])
def create_new_appointment():
    values = request.get_json()
    print(values)

    host_id = values['host_id']
    guest_id = values['guest_id']
    date_offered = values['date_offered']

    vp.add_new_appointment(host_id, guest_id, date_offered)

    jsonable_aptmts = [aptmt.__dict__ for aptmt in vp.get_all_appointments()]
    return jsonify(jsonable_aptmts), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

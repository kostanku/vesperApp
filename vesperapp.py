from appointment import Appointment


class VesperApp:

    def __init__(self):
        self.all_appointments = []
        self.initialize()

    def add_new_appointment(self, host_id, guest_id, date_offered):
        new_appointment = Appointment(host_id, guest_id, date_offered)
        self.all_appointments.append(new_appointment)

    def get_host_appointments(self, host_id):
        return [aptmt for aptmt in self.all_appointments
                if host_id == aptmt.host_id]

    def get_guest_appointments(self, guest_id):
        return [aptmt for aptmt in self.all_appointments
                if guest_id == aptmt.guest_id]

    def get_all_appointments(self):
        return self.all_appointments

    def initialize(self):
        self.add_new_appointment("SteffenID", "AndiID", "dateVorschlag")
        self.add_new_appointment("UlrikeID", "EstherID", "dateVorschlag")
        self.add_new_appointment("UlrikeID", "AndiID", "dateVorschlag")

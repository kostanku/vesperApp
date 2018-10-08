import uuid


class Appointment:

    def __init__(self, host_id, guest_id, date_offered):
        self.id = str(uuid.uuid4())
        self.host_id = host_id
        self.guest_id = guest_id
        self.date_offered = date_offered
        self.date_agreed = ''
        print(self)

    def __repr__(self):
        return str(self.__dict__)

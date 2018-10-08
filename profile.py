import uuid


class Profile:

    def __init__(self, email, pwd, name):
        self.id = str(uuid.uuid4())
        self.email = email
        self.pwd = pwd
        self.name = name

    def __repr__(self):
        return str(self.__dict__)


class UserModel:
    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name

    def __str__(self):
        return f"UserModel(name='{self.name}', email='{self.email}')"

class UserModel:
    def __init__(self, email, name):
        self.email = email
        self.name = name

    def __str__(self):
        return f"UserModel(name='{self.name}', email='{self.email}')"
import bcrypt
from user import User


class AuthManager:
    def __init__(self):
        self.user_model = User()
        self.currect_user = None

    def login(self, username, password):
        user = self.user_model.get_by_username(username)
        if user and self.verify_password(password, user[0][2]):
            self.currect_user = user
            return True
        return False

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password, hash_password):
        return password == hash_password

        # return bcrypt.checkpw(password.encode(), hash_password.encode())

    def logout(self):
        self.currect_user = None




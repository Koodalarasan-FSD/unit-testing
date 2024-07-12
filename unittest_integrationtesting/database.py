# database.py
class Database:
    def __init__(self):
        self.users = []

    def save_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users

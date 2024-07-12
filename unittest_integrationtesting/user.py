# user.py
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_database(self):
        from database import Database
        db = Database()
        db.save_user(self)


# test_integration.py
import unittest
from user import User
from database import Database

class TestUserDatabaseIntegration(unittest.TestCase):

    def setUp(self):
        # Initialize a fresh database instance for each test
        self.db = Database()

    def test_save_user_to_database(self):
        user = User('john_doe', 'john@example.com')
        user.save_to_database()
        users_in_db = self.db.get_users()
        
        self.assertEqual(len(users_in_db), 1)
        self.assertEqual(users_in_db[0].username, 'john_doe')
        self.assertEqual(users_in_db[0].email, 'john@example.com')

    def test_multiple_users_to_database(self):
        user1 = User('alice', 'alice@example.com')
        user2 = User('bob', 'bob@example.com')

        user1.save_to_database()
        user2.save_to_database()

        users_in_db = self.db.get_users()

        self.assertEqual(len(users_in_db), 2)
        self.assertEqual(users_in_db[0].username, 'alice')
        self.assertEqual(users_in_db[1].username, 'bob')

if __name__ == '__main__':
    unittest.main()

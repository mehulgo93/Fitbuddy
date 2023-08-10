import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(name="Alice", age=25, height_cm=160, weight_lb=55)

    def test_name_property(self):
        self.assertEqual(self.user.name, "Alice")
        self.user.name = "Bob"
        self.assertEqual(self.user.name, "Bob")

    def test_age_property(self):
        self.assertEqual(self.user.age, 25)
        self.user.age = 30
        self.assertEqual(self.user.age, 30)

    def test_weight_lb_property(self):
        self.assertEqual(self.user.weight_lb, 55)
        self.user.weight_lb = 60
        self.assertEqual(self.user.weight_lb, 60)

if __name__ == "__main__":
    unittest.main()


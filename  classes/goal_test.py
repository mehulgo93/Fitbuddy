import unittest
from unittest.mock import MagicMock
from goal import Goal

class TestGoal(unittest.TestCase):
    def setUp(self):
        self.mock_user = MagicMock()

    def test_goal_initialization(self):
        goal = Goal(user=self.mock_user, description="Lose weight", target_value=5, unit="kg")
        self.assertEqual(goal.user, self.mock_user)
        self.assertEqual(goal.description, "Lose weight")
        self.assertEqual(goal.target_value, 5)
        self.assertEqual(goal.unit, "kg")

    def test_goal_user_property(self):
        goal = Goal(user=self.mock_user, description="Lose weight", target_value=5, unit="kg")
        self.assertEqual(goal.user, self.mock_user)

    def test_goal_description_property(self):
        goal = Goal(user=self.mock_user, description="Lose weight", target_value=5, unit="kg")
        self.assertEqual(goal.description, "Lose weight")

    def test_goal_target_value_property(self):
        goal = Goal(user=self.mock_user, description="Lose weight", target_value=5, unit="kg")
        self.assertEqual(goal.target_value, 5)

    def test_goal_unit_property(self):
        goal = Goal(user=self.mock_user, description="Lose weight", target_value=5, unit="kg")
        self.assertEqual(goal.unit, "kg")

if __name__ == '__main__':
    unittest.main()

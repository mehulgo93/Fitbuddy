import unittest
from unittest.mock import MagicMock
from workout import Workout

class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.mock_user = MagicMock()

    def test_init(self):
        workout = Workout(date="2023-08-01", user=self.mock_user, duration_minutes=60)
        self.assertEqual(workout.date, "2023-08-01")
        self.assertEqual(workout.user, self.mock_user)
        self.assertEqual(workout.duration_minutes, 60)
        self.assertEqual(workout.exercises, [])

    def test_add_exercises(self):
        workout = Workout(date="2023-08-01", user=self.mock_user, duration_minutes=60)
        mock_exercise = MagicMock()
        workout.add_exercises(mock_exercise, sets=3, repetitions=10)
        self.assertEqual(len(workout.exercises), 1)
        self.assertEqual(workout.exercises[0]["exercise"], mock_exercise)
        self.assertEqual(workout.exercises[0]["sets"], 3)
        self.assertEqual(workout.exercises[0]["repetitions"], 10)

if __name__ == "__main__":
    unittest.main()

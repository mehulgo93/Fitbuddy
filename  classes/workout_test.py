import unittest
from unittest.mock import MagicMock
from workout import Workout

class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.mock_user = MagicMock()
    
    def test_workout_initialization(self):
        workout = Workout(date="2023-08-01", user=self.mock_user)
        self.assertEqual(workout.date, "2023-08-01")
        self.assertEqual(workout.user, self.mock_user)
        self.assertEqual(workout.exercises, [])
        
    def test_add_exercises(self):
        workout = Workout(date="2023-08-01", user=self.mock_user)
        mock_exercise = MagicMock()
        print("Before adding exercise:", workout.exercises)
        workout.add_exercises(mock_exercise, sets=3, repetitions=10)
        print("After adding exercise:", workout.exercises)
    
        self.assertEqual(len(workout.exercises), 1)
if __name__ == "__main__":
    unittest.main()
import unittest
from exercise import Exercise

class TestExercise(unittest.TestCase):
    def test_valid_exercise(self):
        exercise = Exercise(name="Running", exercise_type="Cardio", duration_minutes=30, intensity=7)
        self.assertEqual(exercise.name, "Running")
        self.assertEqual(exercise.exercise_type, "Cardio")
        self.assertEqual(exercise.duration_minutes, 30)
        self.assertEqual(exercise.intensity, 7)

    def test_invalid_exercise_type(self):
        with self.assertRaises(ValueError):
            Exercise(name="Running", exercise_type="InvalidType", duration_minutes=30, intensity=7)

    def test_invalid_intensity(self):
        with self.assertRaises(ValueError):
            Exercise(name="Running", exercise_type="Cardio", duration_minutes=30, intensity="high")

if __name__ == "__main__":
    unittest.main()

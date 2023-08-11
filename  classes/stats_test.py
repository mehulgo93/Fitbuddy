import unittest
from unittest.mock import MagicMock
from stats import Statistics
from workout import Workout
from nutrition import Nutrition

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # Mock Workout instances
        self.mock_workouts = [
            MagicMock(duration=30),
            MagicMock(duration=45),
            MagicMock(duration=60)
        ]
        
        # Mock Nutrition instances
        self.mock_nutrition_logs = [
            MagicMock(calories=300),
            MagicMock(calories=500),
            MagicMock(calories=400)
        ]

    def test_calculate_average_workout_duration(self):
        stats = Statistics(workouts=self.mock_workouts, nutrition_logs=[])
        average_duration = stats.calculate_average_workout_duration()
        print(average_duration, "Calculated average workout duration")
        self.assertEqual(average_duration, (30 + 45 + 60) / 3)

    def test_calculate_total_calories_consumed(self):
        stats = Statistics(workouts=[], nutrition_logs=self.mock_nutrition_logs)
        total_calories = stats.calculate_total_calories_consumed()
        self.assertEqual(total_calories, 300 + 500 + 400)

if __name__ == '__main__':
    unittest.main()


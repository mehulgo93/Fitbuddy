import unittest
from nutrition import Nutrition

class TestNutrition(unittest.TestCase):

    def test_valid_nutrition_instance(self):
        nutrition = Nutrition(user="Alice", date="2023-08-01", calories=300, protein=20, carbs=40, fat=10)
        self.assertEqual(nutrition.user, "Alice")
        self.assertEqual(nutrition.date, "2023-08-01")
        self.assertEqual(nutrition.calories, 300)
        self.assertEqual(nutrition.protein, 20)
        self.assertEqual(nutrition.carbs, 40)
        self.assertEqual(nutrition.fat, 10)

    def test_invalid_protein_type(self):
        with self.assertRaises(ValueError):
            nutrition = Nutrition(user="Alice", date="2023-08-01", calories=300, protein="invalid", carbs=40, fat=10)

    def test_invalid_carbs_type(self):
        with self.assertRaises(ValueError):
            nutrition = Nutrition(user="Alice", date="2023-08-01", calories=300, protein=20, carbs="invalid", fat=10)

    def test_invalid_fat_type(self):
        with self.assertRaises(ValueError):
            nutrition = Nutrition(user="Alice", date="2023-08-01", calories=300, protein=20, carbs=40, fat="invalid")

if __name__ == '__main__':
    unittest.main()

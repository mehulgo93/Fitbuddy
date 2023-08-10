class Statistics:
    def __init__(self, workouts, nutrition_logs):
        self.workouts = workouts
        self.nutrition_logs = nutrition_logs
    
    def calculate_average_workout_duration(self):
        total_duration = sum(workout.duration for workout in self.workouts)
        return total_duration / len(self.workouts)
    
    def calculate_total_calories_consumed(self):
        total_calories = sum(nutrition.calories for nutrition in self.nutrition_logs)
        return total_calories

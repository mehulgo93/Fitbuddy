from classes.user import User
from classes.exercise import Exercise
from classes.workout import Workout
from classes.nutrition import Nutrition
from classes.sleeplog import SleepLog
from classes.visualization import Visualization

def main():
    print("Welcome to FitBuddy Fitness Tracker App!")

    # Create a user
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight_lb = float(input("Enter your weight (lbs): "))
    height_cm = float(input("Enter your height (cm): "))
    user = User(name, age, weight_lb, height_cm)

    # Log exercise
    print("\nLog an exercise:")
    exercise_name = input("Enter exercise name: ")
    exercise_type = input("Enter exercise type: ")
    duration_minutes = int(input("Enter duration (minutes): "))
    intensity = input("Enter intensity: ")
    exercise = Exercise(exercise_name, exercise_type, duration_minutes, intensity)

    # Create a workout
    workout_date = input("\nEnter workout date (YYYY-MM-DD): ")
    workout = Workout(workout_date, user)
    workout.add_exercise(exercise)

    # Log nutrition
    print("\nLog nutrition:")
    calories = int(input("Enter calories consumed: "))
    protein = float(input("Enter protein intake (g): "))
    carbs = float(input("Enter carbs intake (g): "))
    fat = float(input("Enter fat intake (g): "))
    nutrition = Nutrition(user, workout_date, calories, protein, carbs, fat)

    # Log sleep
    print("\nLog sleep:")
    hours_slept = float(input("Enter hours slept: "))
    sleep_quality = input("Enter sleep quality: ")
    sleep_log = SleepLog(user, workout_date, hours_slept, sleep_quality)

    # Display workout progress
    visualization = Visualization()
    visualization.plot_workout_progress(user.name, [workout])

if __name__ == "__main__":
    main()

from user import User
from exercise import Exercise
from workout import Workout
from nutrition import Nutrition
from sleeplog import SleepLog
from goal import Goal
from activityTracker import ActivityTracker
from userSettings import UserSettings
from visualization import Visualization
from interface import FitnessAppGUI


def main():
    # Create instances of various classes
    user = User(name="Alice", age=25, height_cm=160, weight_lb=55)
    exercise = Exercise(name="Running", exercise_type="Cardio", duration_minutes=30, intensity=7)
    workout = Workout(user=user, date="2023-08-01")
    nutrition = Nutrition(user=user, date="2023-08-01", calories=300, protein=20, carbs=40, fat=10)
    sleep_log = SleepLog(user=user, date="2023-08-01", hours_slept=7, sleep_quality="Good")
    goal = Goal(user=user, description="Lose weight", target_value=5, unit="kg")
    activity_tracker = ActivityTracker(user=user)
    user_settings = UserSettings(user=user)
    visualization = Visualization()

    # Simulate app flow
    exercise_instance = exercise  # Use the exercise instance you created above
    workout.add_exercise(exercise_instance)

    # Print workout details
    print(workout)
    print(f"Total workout duration: {workout.get_total_duration()} minutes")
    print("Exercises performed:")
    for exercise in workout.get_exercises():
        print(f"- {exercise.name} ({exercise.duration_minutes} minutes)")

    # ... continue with other simulations ...

if __name__ == "__main__":
    main()

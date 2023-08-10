import matplotlib.pyplot as plt

class Visualization:
    def plot_workout_progress(self, user, workouts):
        dates = [workout.date for workout in workouts]
        durations = [workout.duration for workout in workouts]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, durations, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Duration (minutes)')
        plt.title('Workout Progress Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

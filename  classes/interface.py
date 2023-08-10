import tkinter as tk
from datetime import datetime

class FitnessAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker App")

        # Create widgets
        self.label = tk.Label(root, text="Welcome to Fitness Tracker App")
        self.label.pack()

        self.log_workout_button = tk.Button(root, text="Log Workout", command=self.log_workout)
        self.log_workout_button.pack()

        self.log_nutrition_button = tk.Button(root, text="Log Nutrition", command=self.log_nutrition)
        self.log_nutrition_button.pack()

    def log_workout(self):
        workout_window = tk.Toplevel(self.root)
        workout_window.title("Log Workout")


    def log_nutrition(self):
        nutrition_window = tk.Toplevel(self.root)
        nutrition_window.title("Log Nutrition")

# Create the main application window
root = tk.Tk()
app = FitnessAppGUI(root)
root.mainloop()

class WorkoutLog:
    def __init__(self, user, date):
        self.user = user
        self.date = date
        self.exercises = []

        @property
        def user(self):
            return self._user
        
        @user.setter
        def user(self, value):
            USER_IS_AN_STR = type(value) == str
            if USER_IS_AN_STR:
                self._user = value
        

        @property
        def date(self):
            return self._date
        
        @date.setter
        def date(self, value):
            self._date = value
        

    def add_exercises(self, exercise):
        self.exercises.append(exercise)
    

    def get_total_durations(self):
        total_duration = sum(exercise.duration_minutes for exercise in self.exercises)
        return total_duration
    


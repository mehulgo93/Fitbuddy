
class Workout:
    def __init__(self, date, user, duration_minutes):
        self.user = user
        self.date = date
        self.exercises = []
        self.duration_minutes = duration_minutes

    
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        self._user = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
            self._date = value

    @property
    def duration_minutes(self):
        return self._duration_minutes
    
    @duration_minutes.setter
    def duration_minutes(self, value):
        DURATION_IS_A_FLOAT = isinstance(value, (int, float))
        if DURATION_IS_A_FLOAT:
            self._duration_minutes = float(value)
        else:
            raise ValueError("duration_minutes must be a numeric value (int or float)")

    
    def add_exercises(self, exercise, sets= 1, repetitions= 1):
        EXERCISE_IS_IN_LIST = any(item["exercise"] == exercise for item in self.exercises)
        if not EXERCISE_IS_IN_LIST:
            self.exercises.append({"exercise": exercise, "sets": sets, "repetitions": repetitions})
    


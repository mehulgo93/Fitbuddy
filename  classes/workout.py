
class Workout:
    def __init__(self, date, user):
        self.user = user
        self.date = date
        self.exercises = []

    
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
    
    def add_exercises(self, exercise, sets= 1, repetitions= 1):
        EXERCISE_IS_IN_LIST = any(item["exercise"] == exercise for item in self.exercises)
        if EXERCISE_IS_IN_LIST:
            self.exercises.append({"exercise": exercise, "sets": sets, "repetitions": repetitions})
    


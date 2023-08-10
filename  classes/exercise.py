class Exercise:
    

    EXERCISE_TYPES = ["Cardio", "Strength Training", "Yoga", "CrossFit", "Boxing", "Ju Jitsu",  "Other"]

    def __init__(self, name, exercise_type, duration_minutes, intensity):
        self.name = name
        self.exercise_type = exercise_type
        self.duration_minutes = duration_minutes
        self.intensity = intensity

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        NAME_IS_A_STR = type(value) == str
        if NAME_IS_A_STR:
            self._name = value
    
    @property
    def exercise_type(self):
        return self._exercise_type
    
    @exercise_type.setter
    def exercise_type(self, value):
        EXERCISE_IS_A_STR = type(value) == str
        EXERCISE_IS_IN_LIST = value in Exercise.EXERCISE_TYPES
        if EXERCISE_IS_IN_LIST and EXERCISE_IS_A_STR:
            self._exercise_type = value
        else:
            raise ValueError("Exercise type is invalid")
        
    @property
    def duration_minutes(self):
        return self._duration_minutes
    
    @duration_minutes.setter
    def duration_minutes(self, value):
        MINUTES_IS_AN_INT = type(value) == int
        if MINUTES_IS_AN_INT:
            self._duration_minutes = value
        else:
            raise ValueError("duration_minutes must be an integer which means positive and above zero")
    
    @property
    def intensity(self):
        return self._intensity
    
    @intensity.setter
    def intensity(self, value):
        INTENSITY_IS_AN_INT = type(value) == int
        if INTENSITY_IS_AN_INT:
            self._intensity = value
        else:
            raise ValueError("intensity must be an integer")
    

    

    
    

    


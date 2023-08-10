class ActivityTracker:
    def __init__(self, user):
        self.user = user
        self._steps = 0
        self._distance = 0
        self._active_minutes = 0


    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        self._user = value

    @property
    def steps(self):
        return self._steps
    
    @steps.setter
    def steps(self, steps):
        self._steps += steps
    
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, distance):
        self._distance += distance
    
    @property
    def active_minutes(self):
        return self._active_minutes
    
    @active_minutes.setter
    def active_minutes(self, active_minutes):
        self._active_minutes += active_minutes

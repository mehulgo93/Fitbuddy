class SleepLog:
    def __init__(self, user, date, hours_slept, sleep_quality):
        self.user = user
        self.date = date
        self.hours_slept = hours_slept
        self.sleep_quality = sleep_quality

    @property
    def hours_slept(self):
        return self._hours_slept
    
    @hours_slept.setter
    def hours_slept(self, hours_slept):
        HOURS_SLEPT_IS_AN_INT = type(hours_slept) == int
        if HOURS_SLEPT_IS_AN_INT:
            self._hours_slept = hours_slept
    
    @property
    def sleep_quality(self):
        return self._sleep_quality
    
    @sleep_quality.setter
    def sleep_quality(self, sleep_quality):
        self._sleep_quality = sleep_quality

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
            self._user = user

    @property
    def date(self):
            return self._date
        
    @date.setter
    def date(self, value):
            self._date = value

    def add_entry(self, hours_slept, sleep_quality):
            hours_slept= hours_slept
            sleep_quality= sleep_quality
            self._entries.append(hours_slept, sleep_quality)
        

class Alarm:
    def __init__(self, time, description):
        self.time = time
        self.description = description
    
    def get_time(self):
        return self.time
    
    def get_description(self):
        return self.description
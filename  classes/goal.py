class Goal:
    def __init__(self, user,  description, target_value, unit):
        self.user = user
        self.description = description
        self.target_value = target_value
        self.unit = unit
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        self._user = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
        return self._description
    
    @property
    def target_value(self):
        return self._target_value
    
    @target_value.setter
    def target_value(self, value):
        self._target_value = value
        return self._target_value
    
    @property
    def unit(self):
        return self._unit
    
    @unit.setter
    def unit(self, value):
        self._unit = value
        return self._unit
    
    

    

    

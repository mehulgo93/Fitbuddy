class User:
    def __init__(self, name, age, weight_lb, height_cm):
        self.name = name
        self.age = age
        self.weight_lb = weight_lb
        self.height_cm = height_cm

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        NAME_IS_A_STR = type(value) == str
        if NAME_IS_A_STR:
            self._name = value
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        AGE_IS_AN_INT = type(value) == int
        if AGE_IS_AN_INT:
            self._age= value
    
    @property
    def height_cm(self):
        return self._height_cm
    
    @height_cm.setter
    def height_cm(self, value):
        HEIGHT_IS_WITHIN_APPROPRIATE_RANGE = (50 < value > 220)
        if HEIGHT_IS_WITHIN_APPROPRIATE_RANGE:
            self._height_cm = value
    
    @property
    def weight_lb(self):
        return self._weight_lb
    
    @weight_lb.setter
    def weight_lb(self, value):
        WEIGHT_IS_WITHIN_APPROPRIATE_RANGE = (50 < value < 800)
        if WEIGHT_IS_WITHIN_APPROPRIATE_RANGE:
            self._weight_lb = value
    
    


    
    
   

    

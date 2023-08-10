class UserSettings:
    def __init__(self, user):
        self.user = user
        self.measurement_unit = "metric"  # Default measurement unit
        self.receive_notifications = True  # Default notification preference
    
    def get_measurement_unit(self):
        return self.measurement_unit
    
    def set_measurement_unit(self, unit):
        self.measurement_unit = unit
    
    def get_notification_preference(self):
        return self.receive_notifications
    
    def set_notification_preference(self, preference):
        self.receive_notifications = preference

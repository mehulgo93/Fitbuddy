class Reminder:
    def __init__(self, title, description, date_time):
        self.title = title
        self.description = description
        self.date_time = date_time
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_date_time(self):
        return self.date_time

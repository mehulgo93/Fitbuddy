import unittest
from reminder import Reminder

class TestReminder(unittest.TestCase):
    def test_reminder_initialization(self):
        reminder = Reminder(title="Meeting", description="Team meeting at 3 PM", date_time="2023-08-10 15:00")
        self.assertEqual(reminder.title, "Meeting")
        self.assertEqual(reminder.description, "Team meeting at 3 PM")
        self.assertEqual(reminder.date_time, "2023-08-10 15:00")

    def test_get_title(self):
        reminder = Reminder(title="Meeting", description="Team meeting at 3 PM", date_time="2023-08-10 15:00")
        self.assertEqual(reminder.get_title(), "Meeting")

    def test_get_description(self):
        reminder = Reminder(title="Meeting", description="Team meeting at 3 PM", date_time="2023-08-10 15:00")
        self.assertEqual(reminder.get_description(), "Team meeting at 3 PM")

    def test_get_date_time(self):
        reminder = Reminder(title="Meeting", description="Team meeting at 3 PM", date_time="2023-08-10 15:00")
        self.assertEqual(reminder.get_date_time(), "2023-08-10 15:00")

if __name__ == '__main__':
    unittest.main()

import unittest
from models import BirthdayReminder, AdvancedBirthdayReminder
from datetime import datetime, timedelta


class TestBirthdayReminder(unittest.TestCase):
    def test_basic_reminder_today(self):
        today = datetime.today().strftime("%Y-%m-%d")
        reminder = BirthdayReminder("TestUser", today)
        message = reminder.get_message()
        self.assertIn("Today is TestUser's birthday!", message)

    def test_advanced_reminder_days_left(self):
        future_date = (datetime.today() + timedelta(days=5)).strftime("%Y-%m-%d")
        reminder = AdvancedBirthdayReminder("FutureUser", future_date)
        message = reminder.get_message()
        self.assertIn("in 5 days", message)

    def test_advanced_reminder_past(self):
        past_date = (datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d")
        reminder = AdvancedBirthdayReminder("PastUser", past_date)
        message = reminder.get_message()
        self.assertIn("was 3 days ago", message)


if __name__ == "__main__":
    unittest.main()

from models import BirthdayReminder, AdvancedBirthdayReminder

# Factory Design Pattern
class ReminderFactory:
    @staticmethod
    def create_reminder(reminder_type, name, birthdate):
        if reminder_type == "basic":
            return BirthdayReminder(name, birthdate)
        elif reminder_type == "advanced":
            return AdvancedBirthdayReminder(name, birthdate)
        else:
            raise ValueError("Unknown reminder type.")

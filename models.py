from abc import ABC, abstractmethod
from datetime import datetime


# Abstraction: Define a base abstract class for reminders
class Reminder(ABC):
    def __init__(self, name, birthdate):
        self._name = name  # Encapsulation: use protected attribute
        self._birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    @abstractmethod
    def get_message(self):
        pass

    def get_name(self):
        return self._name

    def get_birthdate(self):
        return self._birthdate.date()


# Inheritance + Polymorphism: Extend Reminder for different types
class BirthdayReminder(Reminder):
    def get_message(self):
        today = datetime.today().date()
        if self.get_birthdate().month == today.month and self.get_birthdate().day == today.day:
            return f"🎉 Today is {self.get_name()}'s birthday!"
        else:
            return f"{self.get_name()}'s birthday is on {self.get_birthdate()}."


class AdvancedBirthdayReminder(Reminder):
    def get_message(self):
        days_remaining = (self.get_birthdate().replace(year=datetime.today().year) - datetime.today().date()).days
        if days_remaining == 0:
            return f"🎉 Today is {self.get_name()}'s birthday!"
        elif days_remaining > 0:
            return f"{self.get_name()}'s birthday is in {days_remaining} days."
        else:
            return f"{self.get_name()}'s birthday was {(abs(days_remaining))} days ago."


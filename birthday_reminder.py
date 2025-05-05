from data_manager import DataManager
from reminder_factory import ReminderFactory
import webbrowser
import random
import time

# 🎥 Personalized video links
def get_personal_video(name):
    videos = {
        "Zamin": "https://www.youtube.com/watch?v=1Ljjcnp4fMI",
         "Nihad": "https://www.youtube.com/watch?v=i-9BrroLW5c",
         "Sean": "https://www.youtube.com/watch?v=Jiy4BYZDjYo",
         "Ali": "https://www.youtube.com/watch?v=9a83Z4AruA4",  # 😄
         "Jafar": "https://www.youtube.com/watch?v=URWeviK1tmE"
    }
    return videos.get(name, "https://www.youtube.com/watch?v=liJicpn4FM")

# ✨ Fun compliment
def get_random_birthday_wish():
    wishes = [
        "May your code always compile on the first try! 💖",
        "Wishing you less bugs and more cake! 🎂",
        "Another year closer to becoming a senior dev 😎",
        "You're a Python pro and a birthday star 🌟",
        "May your life be as clean as your syntax! 🧼"
    ]
    return random.choice(wishes)

# 🎂 Birthday ASCII Cake
def print_cake(name):
    cake = f"""
        ,   ,   ,   ,
       /////|\\\\\\\\\\
      ///// | \\\\\\\\
      |~~~|.|.|.|~~~|
      |  Happy B-day |
      |  {name.center(13)} |
      |___|_|_|_|___|
    """
    print(cake)

# ⌨️ Typewriter effect
def animated_message(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()

# 🔁 Main program
def main():
    data_manager = DataManager()
    birthday_data = data_manager.read_birthdays("birthdays.txt")

    if not birthday_data:
        print("No birthdays found.")
        return

    messages = []
    shown_video = False

    for name, birthdate, reminder_type in birthday_data:
        try:
            reminder = ReminderFactory.create_reminder(reminder_type, name, birthdate)
            message = reminder.get_message()
            print(message)
            messages.append(message)

            if "Today is" in message and not shown_video:
                # 🎂 Show cake
                print_cake(name)

                # 🎉 Surprise message
                print("✨ Birthday Bonus Message:")
                animated_message(get_random_birthday_wish())

                # 🎥 Open video
                print(f"Opening birthday video for {name}...")
                webbrowser.open(get_personal_video(name))

                shown_video = True  # prevent duplicates

        except ValueError as e:
            print(f"Error for {name}: {e}")

    data_manager.write_log("log.txt", messages)


if __name__ == "__main__":
    main()

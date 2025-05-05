class DataManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataManager, cls).__new__(cls)
        return cls.__instance

    def read_birthdays(self, filename):
        birthdays = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        name, birthdate, reminder_type = parts
                        birthdays.append((name.strip(), birthdate.strip(), reminder_type.strip()))
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return birthdays

    def write_log(self, filename, messages):
     with open(filename, "a", encoding="utf-8") as file:  # ✅ Fixes Unicode issue
        for msg in messages:
            file.write(msg + "\n")

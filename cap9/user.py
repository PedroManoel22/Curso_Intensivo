from datetime import datetime


class User:
    def __init__(self):
        self.first_name = "Pedro"
        self.last_name = "Miguel"
        self.age = 18
        self.height = 1.75
        self.nationality = "Brasileiro"
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"\n-----user Information-----\n"
            f"First name: {self.first_name}\n"
            f"Last name: {self.last_name}\n"
            f"Age: {self.age}\n"
            f"Height: {self.height}\n"
            f"Nationality: {self.nationality}\n"
        )

    def greet_user(self):
        now = datetime.now()
        only_time = now.strftime("%H%M")
        only_time = int(only_time)

        # good morning
        if only_time >= 500 and only_time <= 1159:
            greet = "good morning"

        # good afternoon
        elif only_time >= 1200 and only_time <= 1759:
            greet = "good afternoon"

        # goodnight
        else:
            greet = "goodnight"

        print(f"{greet} {self.first_name}, welcome!")

    def increment_login_attemps(self):
        self.login_attempts += 1
        print(f"\n{self.login_attempts}")

    def reset_login_attemps(self):
        self.login_attempts = 0
        print(f"\n{self.login_attempts}")


if __name__ == "__main__":
    user1 = User()
    user1.describe_user()
    user1.greet_user()
    user1.increment_login_attemps()
    user1.increment_login_attemps()
    user1.increment_login_attemps()
    user1.reset_login_attemps()
    user1.increment_login_attemps()

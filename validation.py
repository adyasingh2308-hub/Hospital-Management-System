from datetime import datetime


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_age(prompt="Enter age: "):
    while True:
        value = input(prompt).strip()
        try:
            age = int(value)
            if 0 <= age <= 120:
                return age
            print("Age must be between 0 and 120.")
        except ValueError:
            print("Please enter a valid age.")


def get_phone(prompt="Enter 10-digit phone number: "):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and len(phone) == 10:
            return phone
        print("Phone number must contain exactly 10 digits.")


def get_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")
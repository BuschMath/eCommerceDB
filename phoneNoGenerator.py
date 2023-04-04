import random

class phoneNoGenerator:
    def generate_random_phone_number():
        area_code = f"{random.randint(2, 9)}{random.randint(0, 8)}{random.randint(0, 9)}"  # generate a random area code
        first_three = f"{random.randint(2, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"  # generate the first three digits of the phone number
        last_four = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"  # generate the last four digits of the phone number
        phone_number = f"({area_code}) {first_three}-{last_four}"  # format the phone number with parentheses and dashes
        return phone_number
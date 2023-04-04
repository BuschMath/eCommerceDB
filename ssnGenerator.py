import random

class ssnGenerator:
    def generate_random_ssn():
        area_number = random.randint(1, 899) + 100  # generate a random area number between 100 and 999
        group_number = random.randint(1, 99)  # generate a random group number between 01 and 99
        serial_number = random.randint(1, 9999)  # generate a random serial number between 0001 and 9999
        ssn = f"{area_number:03d}-{group_number:02d}-{serial_number:04d}"  # format the SSN as a string with dashes
        return ssn
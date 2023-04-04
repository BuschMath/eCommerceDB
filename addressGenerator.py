import random
import string

class addressGenerator:
    def generate_random_house_number():
        house_number = str(random.randint(1, 9999)).zfill(4)  # generate a random 4-digit number and pad it with zeros if necessary
        return house_number
    
    def generate_random_streetCityStateCountry_name():
        street_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(3, 25)))  # generate a random string of letters between 3 and 25 characters long
        return street_name
    

import random
import string

class nameGenerator:
    def generate_random_name():
        name_length = random.randint(3, 16)
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for _ in range(name_length))
        return name.capitalize()
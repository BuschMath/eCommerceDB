import random
import datetime

class dateGenerator:
    def generate_random_date():
        start_date = datetime.date(1950, 1, 1)  # choose a start date for the random range
        end_date = datetime.date.today()  # choose the current date as the end date for the random range
        random_date = start_date + (end_date - start_date) * random.random()  # generate a random date between start_date and end_date
        return random_date.strftime("%Y-%m-%d")  # format the date as YYYY-MM-DD
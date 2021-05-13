from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


class BirthDay:

    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def age(self):
        present_time = datetime.now()
        birth_day = datetime(self.year, self.month, self.day, self.hour)
        if present_time > birth_day:
            year = present_time.year - self.year
        else:
            print("You are not BORN yet.")

        age_in_days = int((present_time - birth_day).days)
        x = int(present_time.hour - birth_day.hour)
        if int(present_time.hour - birth_day.hour)<0:
            x = 24 + int(present_time.hour - birth_day.hour)
            int(age_in_days)
        else:
            pass
        age_in_hour = x + (int(age_in_days)*24)
        return f'Age to years: {year}  \nAge by the hour: {age_in_hour}\nAge by the days: {age_in_days}\n'

    def time_to_next_birthday(self):
        present_day = datetime.now()
        x = datetime(present_day.year, self.month, self.day, self.hour)
        if int((x - present_day).days) >= 0:
            res = (x - present_day).days
        else:
            res = 365 + int((x - present_day).days)
        return f'{res} days left until next BIRTHDAY!!!'



birth1 = BirthDay(2020, 4, 20, 18)
print(birth1.age())
print(birth1.time_to_next_birthday())
from datetime import datetime, date, timedelta


def check_isvalid(s_day: datetime, e_day: datetime):
    """check the input date and time is valid"""
    s_day = datetime.strptime(s_day, "%d/%m/%Y")
    e_day = datetime.strptime(e_day, "%d/%m/%Y")
    if isinstance(s_day, datetime) and isinstance(e_day, datetime):
        s_day = s_day.date()
        e_day = e_day.date()
    else:
        raise TypeError
    if e_day >= s_day:
        pass
    else:
        raise TypeError
    return s_day, e_day


def weekday_gen(s_day: datetime, e_day: datetime, w_day: int):
    """generator for specified week days between 2 date"""
    if not (isinstance(w_day, int) and 0 <= w_day <= 6):
        raise TypeError
    start_day_w_day = s_day.weekday()
    difference = w_day - start_day_w_day
    if difference < 0:
        difference = difference + 7
    ans = s_day + timedelta(days=difference)

    if ans <= e_day:
        yield ans
    while True:
        ans = ans + timedelta(days=7)
        if ans <= e_day:
            yield ans



try:
    print('this program is a generator for specified week days between 2 date')
    start_date = input('enter start date, based on : day/month/year\n')
    end_date = input('enter end date, based on : day/month/year\n')
    week_day = int(input(
        'enter number of day in week, based on:\n"Monday = 0","Tuesday = 1","Wednesday = 2","Thursday = 3",\n"Friday '
        '= 4","Saturday = 5","Sunday = 6"\n'))
    valid_dates = check_isvalid(start_date, end_date)
    answer = weekday_gen(*valid_dates, week_day)
    while True:
        print(next(answer))
except TypeError:
    print('invalid input data!!!')
except OverflowError:
    print('\ndates is generated!!!\n===end of program===')
except:
    print('unexpected error! ... please check your inputs')

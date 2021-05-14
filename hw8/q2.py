from datetime import datetime, date

import jdatetime


def check_isvalid(first_time: datetime, second_time: datetime):
    """check the input date and time is valid"""
    first_time = datetime.strptime(first_time, "%d/%m/%Y %H:%M:%S")
    second_time = datetime.strptime(second_time, "%d/%m/%Y %H:%M:%S")

    if isinstance(first_time, datetime) and isinstance(second_time, datetime):
        pass
    else:
        raise TypeError
    if second_time >= first_time:
        pass
    else:
        raise Exception
    return first_time, second_time


def differ_time(first_time: datetime, second_time: datetime):
    """this function get 2 date and time. then return difference between them in seconds"""
    difference = second_time - first_time
    seconds = difference.seconds + difference.days * 24 * 3600
    return seconds


def j_date(first_time: datetime, second_time: datetime):
    """turn gregorian calendar date to jalali calendar date"""
    first_date = first_time.date()
    second_date = second_time.date()
    first_date_jalali = jdatetime.date.fromgregorian(date=first_date)
    second_date_jalali = jdatetime.date.fromgregorian(date=second_date)
    first_date_jalali = first_date_jalali.strftime('%d %B %Y')
    second_date_jalali = second_date_jalali.strftime('%d %B %Y')
    return first_date_jalali, second_date_jalali


def calculate_change_hours(first_time: datetime, second_time: datetime):
    """calculate change in hour"""

    first_date_jalali = jdatetime.date.fromgregorian(date=first_time.date())
    second_date_jalali = jdatetime.date.fromgregorian(date=second_time.date())
    first_year_jalali = jdatetime.date.fromgregorian(date=first_time.date()).strftime('%Y')
    second_year_jalali = jdatetime.date.fromgregorian(date=second_time.date()).strftime('%Y')
    arg1 = jdatetime.date(year=int(first_year_jalali), month=1, day=1)
    arg2 = jdatetime.date(year=int(first_year_jalali), month=6, day=31)
    arg3 = jdatetime.date(year=int(second_year_jalali), month=1, day=1)
    arg4 = jdatetime.date(year=int(second_year_jalali), month=6, day=31)

    if first_date_jalali < arg2 and second_date_jalali < arg4:
        answer = (int(second_year_jalali) - int(first_year_jalali)) * 2
        if first_date_jalali == arg1:
            answer += 1

    elif first_date_jalali < arg2 and arg4 <= second_date_jalali:
        answer = ((int(second_year_jalali) - int(first_year_jalali)) * 2) + 1
        if first_date_jalali == arg1:
            answer += 1

    elif arg2 <= first_date_jalali and second_date_jalali < arg4:
        answer = ((int(second_year_jalali) - int(first_year_jalali)) * 2) - 1
        if first_date_jalali == arg2:
            answer += 1

    elif arg2 <= first_date_jalali and arg4 <= second_date_jalali:
        answer = (int(second_year_jalali) - int(first_year_jalali)) * 2
        if first_date_jalali == arg2:
            answer += 1

    return answer


def calculate_leap_years(first_time: datetime, second_time: datetime):
    """calculate leap years between 2 date and time"""
    first_year = first_time.year
    second_year = second_time.year
    cnt = 0
    for year in range(first_year, second_year):
        if is_leap_year(year):
            cnt += 1
    return cnt


def is_leap_year(year: int):
    """Specified a year is leap year or not!!!"""
    year = year
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


try:
    print('===program for determine difference between 2 date and time===\n')
    a = input('first date and time, base on this pattern: \nday/month/year hour:minute:second\n')
    b = input('second date and time, base on this pattern: \nday/month/year hour:minute:second\n')
    x = check_isvalid(a, b)
    answer1 = differ_time(*x)
    print('difference in seconds = ', answer1)
    answer2 = j_date(*x)
    print('first date in jalali calender = ', answer2[0], '\nsecond date in jalali calender = ', answer2[1])
    answer3 = calculate_leap_years(*x)
    print('leap years = ', answer3)
    answer4 = calculate_change_hours(*x)
    print('number of changes in hour between this 2 date in Iran =', answer4)
except ValueError:
    print('ERORR!!! the input is invalid! please enter input based on given pattern!!!')
except TypeError:
    print('ERORR!!! the input is not date and time Type')
except Exception:
    print('ERORR!!! the input is invalid! second date and time must be earlier than first date and time!!!')
except:
    print('SORRY, unexpected error!')


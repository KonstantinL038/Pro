from datetime import date


# Task 6
def get_date_range(start, end):
    lst = []
    if start > end:
        return lst
    else:
        for k in range(start.toordinal(), end.toordinal() + 1):
            lst.append(date.fromordinal(k))
        return lst


# Task 7
def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start

    sut = 0
    for k in range(start.toordinal(), end.toordinal()+1):
        if date.fromordinal(k).isoweekday() == 6:
            sut += 1
    return sut


date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))
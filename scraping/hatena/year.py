from datetime import date, timedelta

def all_days(year, month, day):
    d = date(year, month, day)
    while d.year == year:
        yield d
        d += timedelta(days=1)


for d in all_days(2019, 11, 1):
    print(d.strftime('%Y%m%d'))
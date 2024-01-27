import datetime as dt


def datum(data):
    dm = [int(a) for a in data]
    date = dt.datetime(2009, dm[1], dm[0])
    print(date.strftime("%A"))
datum(input().split())


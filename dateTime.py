import calendar
from datetime import date, datetime, timedelta

import pytz
from pytz import timezone

from botConfig import botTimeZone


def getTime():
    now = datetime.now(pytz.timezone(botTimeZone))
    myTimeZone = " EST"
    hour = str(now.hour)
    minute = str(now.minute)
    if now.hour >= 12:
        ampm = ' PM'
    else:
        ampm = ' AM'
    if now.hour > 12:
        hour = str(now.hour - 12)
        return "The time is now " + hour + ":" + minute + ampm + myTimeZone


def getDate():
    now = datetime.now(pytz.timezone(botTimeZone))
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    weekday = now.weekday()
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    weekdayName = week[weekday]
    return "Today is " + weekdayName + ", " + mm + "/" + dd + "/" + yyyy

print("Hello there!")
print(getTime())
print(getDate())
import datetime
import calendar


def calendar_module(s):
    # create a tuple from date provided and unpack into 3 variables
    # use Datetime to create the date
    # print the date using the datetime format "%A"

    # create a tuple from date provided and unpack into 3 variables
    month, day, year = tuple(s.split(" "))
    # use Datetime to create the date
    date = datetime.datetime(int(year), int(month), int(day))

    # print the date using the datetime format "%A"
    print(date.strftime("%A").upper())

    # This works but it's not the calendar_module
    # Using calendar_module


calendar_module("08 05 2015")

"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""


import sys
import calendar
from datetime import datetime

c = calendar.TextCalendar(calendar.SUNDAY)
date = datetime.now()
num = input('Enter month then year seperated by a comma:').split(',')
y = [int(i) for i in num if len(num) >= 1]

if len(y) >= 2:
    month = y[0]
    year = y[1]
    str = c.formatmonth(year, month, 0, 0)
    print(str)
elif len(y) == 1:
    month = y[0]
    str = c.formatmonth(date.year, month)
    print(str)
elif len(y) == 0:
    str = c.formatmonth(date.year, date.month)
    print(str)

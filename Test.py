import datetime

# from datetime import *

year = int(input("Plaese Enter the year "))

month = int(input("Plaese Enter the month "))

day = int(input("Plaese Enter the dag "))


today = datetime.datetime.now()

print(today)

DOB = datetime.datetime(year,month,day)

age = today - DOB

print(age)

final_age = age.days / 365

print(" your age is: ", int(final_age) )
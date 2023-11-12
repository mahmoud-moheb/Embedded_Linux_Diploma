#!/usr/bin/python3
#Program prints the calendar of a given month and year
import calendar 
y = int(input("Enter the year: "))
m = int(input("Enter the month: "))
print("\n")
print(calendar.month(y,m))

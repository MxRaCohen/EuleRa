"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=19
Description: 
You are given the following information, 
but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, 
  but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_sundays(start: int, stop: int) -> int:
	day = 2  # 1901 started on a Tuesday given that 1900 started on a Monday
	sunday_count = 0

	for year in range(start, stop):
		for month in months:
			day += month
			if year % 4 == 0 and month == 28:
				day += 1
			if day  % 7 == 0:
				sunday_count += 1

	return sunday_count


# Check test solution matches description and generate real answer
print(count_sundays(1901, 2001))

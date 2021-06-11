"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=16
Description: 
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

# Adds together the individual digits of a given number
def sum_digits(n: int) -> int:
	# Converts the number into a string which is a list of its characters
	str_n = str(n)
	# For every character in the string, cast the digit back to an int
	digit_list = [int(x) for x in str_n]
	# Sum the new list of ints and return
	return sum(digit_list)

# Check test solution matches description and generate real answer
print(sum_digits(2 ** 15)) 
print(sum_digits(2 ** 1000)) 

"""
Author: Ra Cohen (@MxRaCohen)
Date: June 08, 2021
Problem URL: https://projecteuler.net/problem=4
Description: 
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Checks if given number is a palindrome
def is_palindrome(x):
	# Convert the number to a string (list of characters)
	num_list = str(x)

	# if the list of digits is the same forwards and reversed, it's a palindrome
	return num_list == num_list[::-1]

# Finds the largest palindrome made from the product of two numbers
def find_largest_palindrome(upper_bound):
	# lower_bound must be the same length as upper_bound just with a 1 and 0's
	lower_bound = int("1" + "0" * (len(str(upper_bound)) - 1))

	# Initialize output
	palindrome = 0

	# Decrememt from our max to our min
	for x in range(upper_bound, lower_bound + 1, -1):
		# Our second factor needn't be smaller than our first
		for y in range(upper_bound, x, -1):
			# Check that the product is a palindrome and larger 
			if is_palindrome(x * y) and x * y > palindrome:
				palindrome = x * y
				print("{} * {} = {} ".format(x, y, x * y))

	return palindrome

# Check test solution matches description and generate real answer
print(find_largest_palindrome(99))
print(find_largest_palindrome(999))

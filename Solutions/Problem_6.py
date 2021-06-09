"""
Author: Ra Cohen (@MxRaCohen)
Date: June 09, 2021
Problem URL: https://projecteuler.net/problem=6
Description: 
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""

# Inclusively sum the squares
def sum_squares(upper_bound: int) -> int:
	# Initialize answer with additive identity
	ans = 0
	for x in range(upper_bound + 1):
		ans += x ** 2
	return ans

# Inclusively square the sums
def square_sums(upper_bound: int) -> int:
	# Initizalize answer with additive identity
	ans = 0
	for x in range(upper_bound + 1):
		ans += x
	return ans ** 2

# Computes and finds the difference between the above
def square_sum_minus_sum_square(upper_bound: int) -> int:
	sum_square = sum_squares(upper_bound)
	square_sum = square_sums(upper_bound)
	return square_sum - sum_square

# Check test solution matches description and generate real answer
print(square_sum_minus_sum_square(10))
print(square_sum_minus_sum_square(100))
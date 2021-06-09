"""
Author: Ra Cohen (@MxRaCohen)
Date: June 08, 2021
Problem URL: https://projecteuler.net/problem=1
Description: 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_sum_3_and_5(upper_bound: int) -> int:
	# Find the sum of all multiples of 3 under the upperbound
	sum_3 = sum([i for i in range(0, upper_bound, 3)])

	# Find the sum of all multiples of 5 under the upperbound
	sum_5 = sum([i for i in range(0, upper_bound, 5)])

	# Find the sum of all multiples of 15 under the upperbound
	sum_15 = sum([i for i in range(0, upper_bound, 15)])

	# Add sum_3 and sum_5 then subtract the sum_15 to remove duplicated values
	ans = sum_3 + sum_5 - sum_15
	return ans

# or

def find_sum_3_and_5_method_2(upper_bound: int) -> int:
	# Create a list to hold our discovered multiples
	multiples_of_3_or_5 = list()

	for i in range(upper_bound):
		# Determine if current integer is a multiple of 3 or 5
		if i % 3 == 0 or i % 5 == 0:
			# if yes, append it to our list
			multiples_of_3_or_5.append(i)

	# sum up our list to get the answer
	ans = sum(multiples_of_3_or_5)
	return ans

# Check test solutions match description and both methods yeild the same answers
print(find_sum_3_and_5(10))
print(find_sum_3_and_5(1000))
print(find_sum_3_and_5_method_2(10))
print(find_sum_3_and_5_method_2(1000))

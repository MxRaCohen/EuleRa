"""
Author: Ra Cohen (@MxRaCohen)
Date: June 11, 2021
Problem URL: https://projecteuler.net/problem=21
Description: 
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from Problem_12 import factor_num

def d(n: int) -> int:
	factors = factor_num(n)
	factors.pop(factors.index(n))  # removes n from its own list of factors
	return sum(factors)

def check_amicable(a: int, b: int) -> bool:
	if d(a) == b and d(b) == a:
		return True
	return False

def sum_all_amicables_under(upper_bound: int) -> int:
	amicable_set = set()

	for a in range(1, upper_bound):
		b = d(a)
		if check_amicable(a, b):
			amicable_set.add(a)
			amicable_set.add(b)

	return sum(amicable_set)

# Check test solution matches description and generate real answer
print(check_amicable(220, 284))
print(sum_all_amicables_under(10000))

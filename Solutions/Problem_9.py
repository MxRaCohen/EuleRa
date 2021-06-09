"""
Author: Ra Cohen (@MxRaCohen)
Date: June 09, 2021
Problem URL: https://projecteuler.net/problem=9
Description: 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a * b * c.
"""

from Problem_3 import product

# Finds the first Pythagorean triplet which adds up to a given sum
def find_pythag_triplet_with_sum(target: int) -> list[int]:
	for a in range(1, target):
		for b in range(a, target):
			"""
			Note: a**2 + b**2 = c**2 -> (a**2 + b**2)**.5 = c
			thus a + b + c = N = a + b + (a**2 + b**2)**.5
			"""
			if a + b + (a**2 + b**2)**.5 == target:
				return [a, b, int((a**2 + b**2)**.5)]
	return [0, 0, 0]

# Check test solution matches description and generate real answer
print(find_pythag_triplet_with_sum(12))
print(find_pythag_triplet_with_sum(1000))
print(product(find_pythag_triplet_with_sum(1000)))

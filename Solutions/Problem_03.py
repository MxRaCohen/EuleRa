"""
Author: Ra Cohen (@MxRaCohen)
Date: June 08, 2021
Problem URL: https://projecteuler.net/problem=3
Description: 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Takes the product of all elements in a list
def product(num_list: list[int]) -> int:
	# initialize answer with the multiplicative identity
	ans = 1
	for x in num_list:
		ans *= x
	return ans

# Factors a number into a list of its primes
def factor(target: int) -> list[int]:
	# initialize prime list with the multiplicative identity 
	prime_list = [1]

	# initialize number to try with first prime
	number_to_try = 2

	# So long as the primes do not multiply up to the target...
	while product(prime_list) != target:
		# if the target (not including the primelist) is divisible by the new num
		if (target / product(prime_list)) % number_to_try == 0:
			# add the new num to the list of primes
			prime_list.append(number_to_try)
		# if not
		else:
			# try a new number
			number_to_try += 1

	return prime_list

# Finds the largest prime of a number by factoring it
def largest_prime(target: int) -> int:
	prime_list = factor(target)
	# return only the last element of the list
	return prime_list[-1]

# Check test solution matches description and generate real answer
# print(largest_prime(13195))
# print(largest_prime(600851475143))

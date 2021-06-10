"""
Author: Ra Cohen (@MxRaCohen)
Date: June 09, 2021
Problem URL: https://projecteuler.net/problem=5
Description: 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

PrimeFactors = dict[int, int]

# Unfactors a dictionary of primes
def unfactor(prime_dict: PrimeFactors) -> int:
	# Initialize answer with multiplicative identity
	ans = 1
	# For every prime
	for p in prime_dict.keys():
		# multiply the answer by p^count
		ans *= p ** prime_dict[p]
	return ans

# Factors a given number into a dictionary of its primes and counts 
def factor(num: int) -> PrimeFactors:
	# See Problem_3.py for more on this
	primes = dict()
	number_to_try = 2
	while unfactor(primes) != num:
		if num / unfactor(primes) % number_to_try == 0:
			if number_to_try in primes.keys():
				primes[number_to_try] += 1 
			else:
				primes[number_to_try] = 1
		else:
			number_to_try += 1
	return primes

# Combines two prime dicts so that any number divisible by one is divisible by both
def combine_factors(dict_1: PrimeFactors, dict_2: PrimeFactors) -> PrimeFactors:
	# For every number in the first dictionary of factors
	for num in dict_1.keys():
		# Check if it's a factor of the second dictionary
		if num in dict_2.keys():
			# If so, set the value to the max of the two to ensure divisibility 
			dict_2[num] = max(dict_1[num], dict_2[num])
		else:
			# If not, add it
			dict_2[num] = dict_1[num]
	return dict_2

# Finds all primes up to the given upper_bound
def find_primes(upper_bound: int) -> int:
	# Initialize answer dict
	primes = {}

	# Iterate through numbers less than the bound
	for x in range(2, upper_bound + 1):
		primes = combine_factors(primes, factor(x))

	return unfactor(primes)

# Check test solution matches description and generate real answer
print(find_primes(10))
print(find_primes(20))

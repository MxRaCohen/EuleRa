"""
Author: Ra Cohen (@MxRaCohen)
Date: June 09, 2021
Problem URL: https://projecteuler.net/problem=7
Description: 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

# Finds the nth prime for a given n
def find_nth_prime(n):
	# Initialize list of primes with first prime
	prime_list = [2]

	# Initialize first number with first prime
	number_to_try = 2

	# Until we have enough primes...
	while len(prime_list) < n:
		# Assume each number is prime until proven otherwise
		is_prime = True

		# if any primes divide into it, it is not prime
		for p in prime_list:
			if number_to_try % p == 0:
				is_prime = False
				# And we can stop looking/checking
				break

		if is_prime:
			prime_list.append(number_to_try)

		number_to_try += 1

	return prime_list[-1] 

# Check test solution matches description and generate real answer
print(find_nth_prime(6))
print(find_nth_prime(10001))

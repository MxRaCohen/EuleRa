"""
Author: Ra Cohen (@MxRaCohen)
Date: June 09, 2021
Problem URL: https://projecteuler.net/problem=10
Description: 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# Too Slow - Naive Approach
def find_primes_below(upper_bound: int) -> list[int]:
	# Initialize list of primes with first prime
	prime_list = [2]

	# Initialize first number with first odd prime
	number_to_try = 3

	# Until we have enough primes...
	while number_to_try < upper_bound:
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

		# Since all primes beyond 2 are odd, we need only check the odd numbers
		number_to_try += 2

	return prime_list

# Checks prime by modulo candidate by factors smaller than its square root
def check_prime(prime_candidate: int, prime_list: list[int]) -> bool:
	prime_sq_rt = prime_candidate ** 0.5
	for p in prime_list:
		if p > prime_sq_rt:
			break
		if prime_candidate % p == 0:
			return False
	return True

# All prime nums > 3 can be represented by the formula 6n + 1 and 6n -1 for n>=1
def find_primes_below_smart(upper_bound: int) -> list[int]:
	# Initialize list of primes with the first two primes
	prime_list = [2, 3]

	# initialize n
	n = 1

	# Until we have a large enough prime...
	while prime_list[-1] < upper_bound:
		# Consider candidate 1 (gauranteed odd)
		prime_candidate_sub = 6 * n - 1
		if check_prime(prime_candidate_sub, prime_list):
			prime_list.append(prime_candidate_sub)

		prime_candidate_plus = 6 * n + 1
		if check_prime(prime_candidate_plus, prime_list):
			prime_list.append(prime_candidate_plus)		

		n += 1

	return [x for x in prime_list if x < upper_bound]


# Check test solution matches description and generate real answer
print(sum(find_primes_below_smart(10)))
print(sum(find_primes_below_smart(2000000)))

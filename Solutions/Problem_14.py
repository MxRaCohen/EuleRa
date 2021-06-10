"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=14
Description: 
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# Generates and counts Collatz steps until we hit a stop num
def collatz_num(n: int, stop: list[int], counter: int) -> (int, list[int], int):
	counter += 1

	# If we have reached a number in our list of stopping conditions, return
	if n in stop:
		return (n, stop, counter)

	# Otherwise, calculate next step and recurse 
	if n % 2 == 0:
		return collatz_num(n / 2, stop, counter)
	else:
		return collatz_num(3 * n + 1, stop, counter)

# Constructs dict of known length chains and determines longest collatz chain
def longest_collatz_chain(upper_bound: int) -> int:
	# Initialize chain with the corresponding chain length of 1
	chains = {1: 1}

	# Initialize answer with the shortest chain length
	longest_chain_key = 1

	# Check all numbers up until the given bound
	for n in range(1, upper_bound):
		# Find the chain length from n to a step we've seen before
		stopped_n, stop_list, counter = collatz_num(n, chains.keys(), 0)
		# Avoid counting the "seen" step twice
		# len(n -> 1) = len(n -> seen) + len(seen -> 1) - 1
		chains[n] = counter + chains[stopped_n] - 1

		# If this chain is longer than our longest seen chain...
		if chains[n] > chains[longest_chain_key]:
			# update our longest_chain_key accordingly
			longest_chain_key = n

	return longest_chain_key


# Check test solution matches description and generate real answer
print(collatz_num(13, [1], 0)[2])
print(longest_collatz_chain(1000000))

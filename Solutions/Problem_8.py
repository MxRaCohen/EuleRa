"""
Author: Ra Cohen (@MxRaCohen)
Date: June 09, 2021
Problem URL: https://projecteuler.net/problem=8
Description: 
The four adjacent digits in the 1000-digit number that 
have the greatest product are 9 × 9 × 8 × 9 = 5832.

(see input_num below)

Find the thirteen adjacent digits in the 1000-digit number that 
have the greatest product. What is the value of this product?
"""

from Problem_3 import product

input_num = ("73167176531330624919225119674426574742355349194934"
             "96983520312774506326239578318016984801869478851843"
             "85861560789112949495459501737958331952853208805511"
             "12540698747158523863050715693290963295227443043557"
             "66896648950445244523161731856403098711121722383113"
             "62229893423380308135336276614282806444486645238749"
             "30358907296290491560440772390713810515859307960866"
             "70172427121883998797908792274921901699720888093776"
             "65727333001053367881220235421809751254540594752243"
             "52584907711670556013604839586446706324415722155397"
             "53697817977846174064955149290862569321978468622482"
             "83972241375657056057490261407972968652414535100474"
             "82166370484403199890008895243450658541227588666881"
             "16427171479924442928230863465674813919123162824586"
             "17866458359124566529476545682848912883142607690042"
             "24219022671055626321111109370544217506941658960408"
             "07198403850962455444362981230987879927244284909188"
             "84580156166097919133875499200524063689912560717606"
             "05886116467109405077541002256983155200055935729725"
             "71636269561882670428252483600823257530420752963450")

# Finds all n-length windows without a 0
def find_windows_without_0(n: int, input_num: str) -> list[str]:
	window_list = []
	for i in range(len(input_num) - n):
		ith_window = input_num[i : i + n]
		if "0" not in ith_window:
			window_list.append(ith_window)
	return window_list

# Returns the largest possible product from n adjacent numbers in input_num
def find_n_adjacent_product(n: int, input_num: str) -> int:
	# Find all n-length windows that do not contain 0
	windows = find_windows_without_0(n, input_num)

	# Initialize answer with 0
	largest_product = 0

	for window in windows:
		window_product = product([int(x) for x in window])
		if window_product > largest_product:
			largest_product = window_product

	return largest_product

# Check test solution matches description and generate real answer
print(find_n_adjacent_product(4, input_num))
print(find_n_adjacent_product(13, input_num))

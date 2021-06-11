"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=15
Description: 
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from Problem_03 import product

def factorial(n: int) -> int:
	return product(range(1, n + 1))

def n_choose_k(n: int, k: int) -> int:
	return factorial(n) / (factorial(k) * factorial(n - k))
"""
         1
       1   1
     1  *2*  1
   1   3   3   1
  1  4  *6*  4  1
 1  5  10 10   5  1
1  6 15 *20* 15  6  1
"""
# on an n x n square, the distance to travel is always n + n 
# however, we only have n opportunities to decide how to traverse that distance
# thus the number of routes is equal to 2n choose n
def count_routes(n: int) -> int:
	return n_choose_k(2 * n, n)

# Check test solution matches description and generate real answer
print(count_routes(1)) # 2 paths
print(count_routes(2)) # 6 paths
print(count_routes(3)) # 20 paths
print(count_routes(20)) # ?

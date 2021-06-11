"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=67
Description: 
By starting at the top of the triangle below and 
moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

[see Problem_67_triangle.txt]

"""

from Problem_18 import max_path_sum

with open("Problem_67_triangle.txt") as f:
	tri = f.readlines()

# Generate real answer
print(max_path_sum(tri)) # 

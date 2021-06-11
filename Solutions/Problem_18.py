"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=18
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

[see tri_2]

"""

tri_1 = """
3
7 4
2 4 6
8 5 9 3
""".split('\n')[1:-1]

tri_2 = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".split('\n')[1:-1]

def combine_two_arrays(l1: list[int], l2: list[int]) -> list[int]:
	return [(l1[i] + l2[i]) for i in range(len(l1))]

def reduce_array(l1: list[int]) -> list[int]:
	return [max(l1[i], l1[i+1]) for i in range(len(l1) - 1)]

def max_path_sum(raw_tri: list[str]) -> int:
	tri = [[int(x) for x in row.split()] for row in raw_tri]
	sum_tri = tri[-1]
	for row_idx in range(1, len(tri)):
		sum_tri = combine_two_arrays(tri[-(1 + row_idx)], reduce_array(sum_tri))

	return sum_tri[0]

# Check test solution matches description and generate real answer
# print(max_path_sum(tri_1)) # 23
# print(max_path_sum(tri_2)) # ?

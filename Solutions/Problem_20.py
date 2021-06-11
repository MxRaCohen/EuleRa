"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=20
Description: 
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from Problem_15 import factorial
from Problem_16 import sum_digits

# Check test solution matches description and generate real answer
print(sum_digits(factorial(10)))  # 27
print(sum_digits(factorial(100)))  # ?

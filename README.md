# EuleRa
A repo for the first few [project euler](https://projecteuler.net/) solutions.

Solutions are verbose, liberally commented, and aimed at students. 

# Functions

As an exercise, I'm not using any outside packages in this repo. 
Below are the functions resused in the course of solving the problems thus far. 
Each problem that develops a function for further use has its print line commented out for usability. 


## `product` from Problem_03
Takes the product of all elements in a list of numbers
`def product(num_list: list[int]) -> int:`

## `factor_num` from Problem_12
Factors the given integer into a list
`def factor_num(num: int) -> list[int]:`

## `factorial` from Problem_15
Returns the product of 1 to n for any int n 
`def factorial(n: int) -> int:`

## `sum_digits` from Problem_16
Adds together the individual digits of a given number
`def sum_digits(n: int) -> int:`

## `max_path_sum` from Problem_18
Given a balanced triangle of numbers, finds the maximum total from top to bottom of the triangle 
`def max_path_sum(raw_tri: list[str]) -> int:`

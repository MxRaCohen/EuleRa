"""
Author: Ra Cohen (@MxRaCohen)
Date: January 18, 2022
Problem URL: https://projecteuler.net/problem=22
Description: 
Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def name_score(name: str) -> int:
	# lowercase all names
	name_lower = name.lower()

	letters = "'abcdefghijklmnopqrstuvwxyz"
	score = 0
	for letter in name_lower:
		score += letters.index(letter)
	return score

def get_name_list(filename: str) -> [str]:
	with open(filename) as f:
		lines = f.readline()
		my_list = eval('[' + lines + ']')
		my_list.sort()
		return (my_list)


def all_name_scores(filename: str) -> int:
	name_list = get_name_list(filename)
	print((name_list))
	name_scores = [name_score(name) for name in name_list]

	all_score = 0
	for i, score in enumerate(name_scores):
		all_score += (i + 1) * score  # index the name list at 1 for proper multiplication
	return all_score

# Check test solution matches description and generate real answer
print(name_score('COLIN'))

print(all_name_scores("Problem_22_names.txt"))

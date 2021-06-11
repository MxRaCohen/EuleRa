"""
Author: Ra Cohen (@MxRaCohen)
Date: June 10, 2021
Problem URL: https://projecteuler.net/problem=17
Description: 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

digit_dict = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety'
}

def quick_convert(num: int) -> str:
	if num == 0:
		return ''
	elif num % 1000 == 0:
		return quick_convert(num / 1000) + ' thousand'
	elif num % 100 == 0:
		return quick_convert(num / 100) + ' hundred'
	else:
		return digit_dict[num]

def convert_num(num: int) -> str:
	if num in digit_dict.keys() or num %  100 == 0:
		return quick_convert(num)

	reversed_num = str(num)[::-1]
	expanded_num_reversed = []
	for i in range(len(reversed_num)):
		expanded_num_reversed.append(reversed_num[i] + "0" * i)

	# Reverse! Reverse! *blghgh* Reverse! Reverse! *blghghg*
	expanded_num = [quick_convert(int(x)) for x in expanded_num_reversed][::-1]
	str_num = " ".join(expanded_num)

	if 'hundred ' in str_num:
		str_num = str_num.replace('hundred ', 'hundred and ')
	if 'ten ' in str_num:
		str_num = str_num[0: str_num.index('ten ')] + quick_convert(int(reversed_num[1] + reversed_num[0]))

	return str_num

def count_letters(num: int) -> int:
	word_num = convert_num(num)
	num_without_spaces = "".join(word_num.split())
	return len(num_without_spaces)

def count_letters_range(start: int, stop: int) -> int:
	total_letters = 0
	for i in range(start, stop + 1):
		total_letters += count_letters(i)
	return total_letters

# Check test solution matches description and generate real answer
print(convert_num(342)) # three hundred and forty-two
print(convert_num(115)) # one hundred and fifteen

print(count_letters(342)) # 23
print(count_letters(115)) # 20

print(count_letters_range(1, 5)) # 19
print(count_letters_range(1, 1000)) # ?
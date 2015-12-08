#Letter Combinations of a Phone Number

import itertools
import sys

def letterCombinations(digits):
	"""
	:type digits: str
	:rtype: List[str]
	"""
	result = []
	dstr = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
	if digits == '':
		return result
	for i in dstr[int(digits[0])]:
		result.append(i)
	if len(digits) == 1:
		return result

	for i in range(1,len(digits)):
		temp = []
		istr = dstr[int(digits[i])]
		for j in result:
			for k in istr:
				temp.append(j+k)
		result = temp
	return result


#print letterCombinations('2')

print letterCombinations(sys.argv[1])
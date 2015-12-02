#coding=utf-8

import sys

def romanToInt(s):
	rdic = {'I':1, 'V':5, 'X':10,  'L':50,  'C':100,   'D':500,  'M':1000}

	result = 0
	isJump = False
	length = len(s)
	for i in range(length):
		if isJump:
			isJump = False
			continue
		if i+1 != length:
			if s[i] =='I':
				if s[i+1] == 'V':
					result += 4
					isJump = True
					continue
				elif s[i+1] == 'X':
					result += 9
					isJump = True
					continue
				else:
					result += 1
					continue

			if s[i] == 'X':
				if s[i+1] == 'L':
					result += 40
					isJump = True
					continue
				elif s[i+1] == 'C':
					result += 90
					isJump = True
					continue
				else:
					result += 10
					continue

			if s[i] == 'C':
				if s[i+1] =='D':
					result += 400
					isJump = True
					continue
				elif s[i+1] == 'M':
					result += 900
					isJump = True
					continue
				else:
					result += 100
					continue
		result += rdic[s[i]]

	return result


if __name__ == '__main__':
	if len(sys.argv) > 1:
		print romanToInt(sys.argv[1])
#coding=utf-8

import sys

class Solution(object):
	"""
	整数划分问题，将整数n划分为一系列不重复正整数之和,求共有多少种组合。
	例：n=6
	   6=1+5；6=2+4；6=1+2+3;
	   共3种组合。
	   求解506共有多少种组合？
	"""
	def integerDivision(self, num):
		if num < 3:
			return 0
		max_n = num
		max_m = 32
		max_s = (max_n/2)/m-(m/2-1)
		count = [[[0]*max_s]*(max_m+1)]*(max_n+1)]
		for n in range(3, max_n+1):
			if n%2 == 0:
				count[n][2][0] = n/2
			else:
				count[n][2][0] = n/2-1
			

s = Solution()
print s.integerDivision(int(sys.argv[1]))

		
#coding=utf-8

import sys

class Solution(object):

	def mySqrt(self, x):
		"""
		:rtype: int
		"""
		high = x
		low = 0
		mid = x/2
		while mid>=low and mid <=high:			
			if mid * mid > x:
				high = mid-1
			elif mid * mid < x:
				low = mid + 1
			else:
				return mid
			mid = (high+low)/2
		return mid

s = Solution()
print s.mySqrt(int(sys.argv[1]))
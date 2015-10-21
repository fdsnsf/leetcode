#coding=utf-8

import sys

class Solution(object):

	def containNearbyDuplicate(self, nums, k):
		if len(nums) < 2:
			return False
		result = {}
		for i in xrange(len(nums)):
			if len(result.get(nums[i], [])) == 0:
				result[nums[i]]= [i, 0]
			else:
				post = result[nums[i]][0]
				l = result[nums[i]][1]
				n_l = i-post
				if l==0 or l>n_l:
					result[nums[i]][1] = n_l
				result[nums[i]][0] = i
		for s in result.values():
			if s[1]!=0 and s[1]<=k:
				return True
		return False

s = Solution()
print s.containNearbyDuplicate([99,99], 1)
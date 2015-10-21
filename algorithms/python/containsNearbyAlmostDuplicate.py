#coding=utf-8

import sys

class Solution(object):

	def containsNearbyAlmostDuplicate(self, nums, k, t):
		length = len(nums)
		if length < 2:
			return False
		if t < 0:
			return False
		bucket = {}
		for i,v in enumerate(nums):
			bucket_num, off_set = (v/t, 1) if t else (v,0)
			for idx in xrange(bucket_num-off_set, bucket_num+off_set+1):
			    if (idx in bucket) and abs(v-bucket[idx])<=t:
				    return True
			bucket[bucket_num]=v
			if len(bucket) > k:
				del bucket[nums[i-k]/t if t else nums[i-k]]
		return False

s = Solution()
print s.containsNearbyAlmostDuplicate([2,4], 1, 1)
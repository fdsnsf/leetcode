#coding=utf-8

import sys

def threeSum(nums):

	if len(nums) < 3:
		return []

	nums.sort()
	result = []

	nMap = {}
	for i in nums:
		if i in nMap:
			nMap[i] += 1
		else:
			nMap[i] = 1

	length = len(nums)
	for i in range(length):

		for j in range (i, len(nums)):
			r = 0 - nums[i] + nums[j]
			if (nMap[nums[j]]>1 and r == nums[j]):
				result.append([nums[i], nums[j], r])


		

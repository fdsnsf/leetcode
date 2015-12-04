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
		for j in range (i+1, len(nums)):
			r = 0 - nums[i] - nums[j]
			if (nMap[nums[j]]>1 and r == nums[j]) or (r in nMap and r > nums[j]):
				if nums[i] == nums[j] and r == 0 and nMap[0]<3:
					continue
				l = [nums[i], nums[j], r]
				if l not in result:
					result.append(l)
	return result

print threeSum([-1, 0, 1, 2, -1, -4])
print threeSum([1,2,-2,-1])
print threeSum([1,1,-2])
print threeSum([0,0,0])
print threeSum([-1,0,1,0])





		

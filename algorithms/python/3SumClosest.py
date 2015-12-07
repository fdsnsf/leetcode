#coding = utf-8

import bisect
def threeSumClosest(nums, target):
	nums.sort()
	summ = sum(nums[-3:])
	if target >= summ:
		return summ
	length = len(nums)
	result =  sum(nums[:3])
	if result >= target:
		return result
	ta = abs(result-target)
	if ta == 0:
		return result
	for i in range(length-2):
		left = bisect.bisect_left(nums, target - nums[i] - nums[-1], lo = i + 1) #binary search
		if left > i + 1: left -= 1
		for j in range(left, length-1):
			n3 = target - nums[i] - nums[j]
			ind =  bisect.bisect_left(nums , n3, j+1)
			values = [ind-1, ind]
			for val in values:
				if val > j and val < length:
					summ = nums[i] + nums[j] + nums[val]
					if summ == target:
						return target
					if abs(summ - target) < ta:
						result = summ
						ta = abs(summ - target)
			if nums[i] + nums[j] + nums[j+1] > target: break
				
					
	return result


print threeSumClosest([-1,2,1,-4], 1)

print threeSumClosest([0,0,0] ,1)

print threeSumClosest([-79,-95,8,-76,-93,-6,19,-68,-64,21,47,37,-47,-88,-12,23,-99,-63,43,-20,50,-85,-64,-48,91,40,64,-50,38,-17,22,-7,-91,-93,40,-35,72,92,-38,-28,75,99,-10,83,-51,-65,73,59,74,-64,-97,-71,-51,-69,68,50,-97,14,62,88,-28,18,-57,98,-61,45,-92,57,9,-99,-54,-87,63,-90,-63,-70,-62,-24,-32,16,-48,-83,-8,49,-98,61,27,-34,13,-81,32,-100,-4,-46,78,-62,-55,98,15,46,-25,-30,-20],289)

print threeSumClosest([-65,-46,-10,-79,-86,39,40,62,31,-40,-80,-20,-6,8,38,-33,97,-99,-86,8,85,57,78,-92,10,5,84,-15,32,11,-15,-5,-56,86,47,-78,39,88,-86,24,-77,52,-55,16,22,-57,-39,-16,-32,-2,-94,-43,13,-49,77,96,35,-46,-47,10,-57,-73,95,-22,-22,5,-3,81,79,-15,-34,41,-91,26,-15,72,35,100,100,-89,-79,70,8,-99,-45,75,-57,15,34,-16,43,54,-99,39,-42,87,-88,-69,39,15,12,29,71,48,-51,20,-18,-37,95,-81,-71,22,56,-87,90,78,-57,-37,-17,-64,82,-28,-25,-83,75,21,97,35,67,12,55,-91,-63,4,-46,15,-19,-60,41,29,-71,26,25,-85,-15,-81,-53,48,31,28,88,-71,19,83,38,-42,-94,42,62,-43,90,-81,-60,56,-47,34,-60,73,-67,72,-99,-46,-47,10,46,-86,-42],220)
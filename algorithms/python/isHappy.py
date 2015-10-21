
class Solution(object):
	"""
	    A happy number is a number defined by the following process: 
	Starting with any positive integer, replace the number by the sum of the squares of its digits, 
	and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
	a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

	Example: 19 is a happy number
	    1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
	"""

	def isHappy(self, n):
		while n > 9:
			n = self.sumOfNum(n)
		result = (n==1 or n==7)
		return result

	def isHappyV2(self, n):
		"""
		    用快慢指针判断环
		"""
		slow = n
		fast = self.sumOfNum(n)

		while slow != 1:
			if slow == fast:
				return False
			else:
				slow = self.sumOfNum(slow)
				fast = self.sumOfNum(self.sumOfNum(fast))
		return True

	def sumOfNum(self, n):
		result = 0
		while n:
			result += pow(n%10, 2)
			n = n//10
		return result
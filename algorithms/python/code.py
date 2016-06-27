#coding=utf-8

import sys

class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value):
		self.value = value
		self.next = None


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

	"""
	Given a pattern and a string str, find if str follows the same pattern.
	Examples:
        pattern = "abba", str = "dog cat cat dog" should return true.
        pattern = "abba", str = "dog cat cat fish" should return false.
        pattern = "abba", str = "dog dog dog dog" should return false.
	"""
	def wordPattern(self, pattern, str):
		str_list = str.split()
		dict_p = dict()

		if len(pattern) != len(str_list):
			return False
		if len(set(pattern)) != len(set(str_list)):
			return False

		for p,s in zip(pattern, str_list):
			if not dict_p.has_key(p):
				dict_p[p] =  s
			elif dict_p[p] != s:
				return False
		return True

	def wordPatternV2(self, pattern, str):

		str_list = str.split()

		if len(pattern) != len(str_list):
			return False
		if len(set(pattern)) != len(set(str_list)):
			return False

		dict_p, dict_s = {}, {}
		for p,s in zip(pattern, str_list):
			dict_p[p] = dict_p.get(p, 0) + 1
			dict_s[s] = dict_s.get(s, 0) + 1

			if dict_s[s] != dict_p[p]:
				return False
		return True

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


	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		result = head = ListNode(0)
		carry = 0
		while l1 or l2 or carry:
			s = (l1.value if l1 else 0) + (l2.value if l2 else 0) + carry
			head.next = ListNode(s%10)
			carry = s/10

			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
			head = head.next
		return result.next


	def lengthOfLongestSubstring(self, s):
		"""
		:rtype: int
		"""
		max_len, now_len=0, 0
		slow = 0
		for i in range(len(s)):
			#pos = s.find(s[i], slow)
			pos = self.finds(s[i], s, slow, i)
			if pos < i:
				max_len = max(max_len, now_len)
				slow = pos+1
				now_len = i-slow
			now_len += 1
		return max(max_len, now_len)


	def finds(self, s, strs, left, right):
		for i in range(left, right):
			if s == strs[i]:
				return i
		return 0

s = Solution()
#print 'isHappy', s.isHappy(int(sys.argv[1]))
#print 'isHappyV2', s.isHappyV2(int(sys.argv[1]))

#print s.wordPattern('abba', 'dog cat cat dog')
#print s.wordPattern('abba', 'dog dog dog dog')

#nums = [1,2,3,4,5,1,7]
#k = 3
#print s.containNearbyDuplicate([99,99], 1)

#print s.containsNearbyAlmostDuplicate([2,4], 1, 1)

#print s.mySqrt(int(sys.argv[1]))


listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode1.next = listNode2
listNode3 = ListNode(3)
listNode2.next = listNode3
l1 = ListNode(5)
#l1.next = listNode1
l2 = ListNode(5)
#l2.next = listNode2

#result = s.addTwoNumbers(l1, l2)

#while result:
#	print result.value
#	result = result.next

print 'dvdf', s.lengthOfLongestSubstring('dvdf')
print 'a', s.lengthOfLongestSubstring('a')
print 'aabc', s.lengthOfLongestSubstring('aabc')
print '567509450', s.lengthOfLongestSubstring('567509450')




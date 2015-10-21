#coding=utf-8

class Solution(object):
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
print 'dvdf', s.lengthOfLongestSubstring('dvdf')
print 'a', s.lengthOfLongestSubstring('a')
print 'aabc', s.lengthOfLongestSubstring('aabc')
print '567509450', s.lengthOfLongestSubstring('567509450')
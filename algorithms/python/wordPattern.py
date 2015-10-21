#coding=utf-8

class Solution(object):

	def wordPattern(self, pattern, str):

		"""
		Given a pattern and a string str, find if str follows the same pattern.
		Examples:
		    pattern = "abba", str = "dog cat cat dog" should return true.
            pattern = "abba", str = "dog cat cat fish" should return false.
            pattern = "abba", str = "dog dog dog dog" should return false.
        """

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

s = Solution()
print s.wordPattern('abba', 'dog cat cat dog')
print s.wordPattern('abba', 'dog dog dog dog')
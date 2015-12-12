import sys

def removeDuplicateLetters(s):

	strdic = {}
	for i in s:
		if i in strdic:
			strdic[i] += 1
		else:
			strdic[i] = 1
	keys = strdic.keys()
	keys.sort()
	result = ''
	length = len(keys)
	for i in range(len(s)):
		nowStr = s[i]
		if nowStr not in keys:
			continue
		pot = keys.index(nowStr)
		if strdic[nowStr]>1 and keys[0] != i:		
			if pot != length -1:
				afStr = keys[pot+1]
				temp = s[i+1:lastIndex(s, afStr, i)]
				for j in keys:
					if j != nowStr and j in temp:
						strdic[nowStr] -= 1
						break
				else:
					result += nowStr
					strdic[nowStr] = 0
					del keys[pot]
			else:
				strdic[nowStr] -= 1
						
			
		elif  strdic[nowStr] == 1:
			result += nowStr
			strdic[nowStr] = 0
			del keys[pot]
		elif keys[0] == nowStr:
			result += nowStr
			strdic[nowStr] = 0
			if len(keys) == 0:
				return result
			del keys[0]
	return result


def lastIndex(s,afStr, i):
	count = s[i:].count(afStr)
	for j in range(i, len(s)):
		
		if s[j] == afStr:
			count -= 1
		if count == 0:
			return j
		

	return s.index(afStr, i)


#print lastIndex('bcabc','c', 0)
print removeDuplicateLetters(sys.argv[1])
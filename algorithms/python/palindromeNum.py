
import sys

def isPalindrome(x):
	if x < 0:
		return False
	i = 1
	while i  <= x/10:
		i *= 10

	while i >= 1:
		if x%10 == x/i:
			x = (x-x/i*i)/10
		else:
			return False
		i /= 100
	return True

if __name__ == '__main__':
	#print '12021'
	#print isPalindrome(12021)

	if len(sys.argv) > 1:
		print isPalindrome(int(sys.argv[1]))
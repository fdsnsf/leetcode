
import sys

def isPalindrome(x):
	if x < 0:
		return False

	length = 0
	i = x
	while i > 0:
		i /= 10
		length += 1
	print 'length:', length

	s = length - 1
	for k in range(length/2):
		high = x/(10**s)
		low = x % 10
		print 's,high,low', s, high, low
		print x
		if high== low:
			x = x- high*10**s
			x /= 10
			s -= 2
			print x
		else:
			return False
	return True

if __name__ == '__main__':
	#print '12021'
	#print isPalindrome(12021)

	if len(sys.argv) > 1:
		print isPalindrome(int(sys.argv[1]))
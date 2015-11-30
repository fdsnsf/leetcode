import sys

class Zigzag(object):

	def convert(self, s, numRows):
		length = len(s)
		rows = numRows
		"""
		if numRows > 2:
			numRows -= 1
		if length % numRows:
			max_l = length/numRows
		else:
			max_l = length/numRows+1
		if self.isEvenNum(max_l):
			min_l = max_l/2
		else:
			min_l = max_l/2+1
		"""

		result = ''
		key = 0
		r =['' for i in range(rows)]
		tag = True
		while key < length:
			if tag:
				for j in range(rows):
					if key < length:
						r[j] += s[key]
						key += 1
				tag = False
			else:
				for j in range(2, rows):
					if key < length:
						r[numRows-j] += s[key]
						key += 1
				tag = True


		"""
		for i in range(max_l):
			key = i
			for j in range(numRows):
				if not self.isEvenNum(i) and self.isEvenNum(j):
					continue
				else:
					key += numRows/2*i +  +i
				if key < length:
					result += s[key]
		"""
		for k in r:
			result += k
		return result


	def isEvenNum(self, num):
		return False if num%2 else True


#PAYPALISHIRING
#P   A   H   N
#A P L S I I G
#Y   I   R
#PAHNAPLSIIGYIR

if __name__ == '__main__':
	zigzag = Zigzag()
	if len(sys.argv) < 3:
		print 'eg: python zigzag.py PAYPALISHIRING 3'
		sys.exit(0)
	print zigzag.convert(sys.argv[1], int(sys.argv[2]))
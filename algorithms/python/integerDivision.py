#coding=utf-8

import sys

class Solution(object):
	"""
	整数划分问题，将整数n划分为一系列不重复正整数之和,求共有多少种组合。
	例：n=6
	   6=1+5；6=2+4；6=1+2+3;
	   共3种组合。
	   求解506共有多少种组合？
	   算法：动态规划
	           先计算整数3的组合数（1；3=1+2），由整数3的组合数计算出整数4的组合数，
	  以此类推直至计算出整数N的组合数。
	"""
	# num = 506  n_m = 31
	def integerDivision(self, num):
		if num < 3:
			return 0
		max_n = num
		max_m = self.maxM(num)
		max_s = self.countS(max_n, 2)
		count = [([([0]*(max_s+1)) for i in range(max_m+1)])for j in range(max_n+1)]

		#N最小为3，组合数为1
		for n in range(3, max_n+1):
			#计算整数N（3~NUM）划分为2（M=2）个整数之和的组合数
			if n%2:    #N为奇数
				count[n][2][0] = n/2
			else:    #N为偶数
				count[n][2][0] = n/2-1
			for  i in range(1, count[n][2][0]+1):
				count[n][2][i] = 1    #2个数的组合数，且一个数已经确定，则组合数只能为1

			s = 0
			for m in range(3, max_m+1):
				s = self.countS(n, m)
				if s <= 0:     #小于NUM的数可划分的整数个数小于M，所以划分为M个数的组合不存在
					break
				for i in range(1, s+1):    #M个数的组合数由NUM前若干个数（即为s）的M-1个数的组合数决定
					temp = 0
					for j in range(1, i+1):
						temp += count[n-i][m-1][j]
					count[n][m][i] = count[n-i][m-1][0] - temp
					count[n][m][0] += count[n][m][i]    #M个数的组合数

		#M个数的组合数
		for j in range(2, max_m):
			count[max_n][max_m][0] += count[max_n][j][0]

		return count[max_n][max_m][0]    #输出总的组合数
 
	def  countS(self, n, m):
		"""
		计算S
		"""
		s = 0
		if m % 2:
			s = n/m - m/2
		else:
			s = (n-m/2)/m - (m/2-1)
		return s

	def maxM(self, n):
		m = 2
		while n > m*(m+1)/2:
			m = m+1

		return m if n==m*(m+1)/2 else m-1
			

s = Solution()
#print s.maxM(int(sys.argv[1]))
print s.integerDivision(int(sys.argv[1]))

		
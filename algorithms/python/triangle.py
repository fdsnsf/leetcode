#coding=utf-8

import sys

#	2
#          3 (5)    4(6)
#       6 (11)    5(10)    7(13)
#     4 (15)   1(11)     8(18)    3(16)
#  2+3+5+1 = 11
def minimumTotal(triangle):
	result = 0
	length = len(triangle)
	ischange = False
	if length == 1:
		return triangle[0][0]
	for i in range(1, len(triangle)):
		li = len(triangle[i])
		for j in range(li):
			if  j == li-1:
				triangle[i][j] += triangle[i-1][j-1]
			elif j == 0:
				triangle[i][j] += triangle[i-1][j]
			else:
				triangle[i][j] += (triangle[i-1][j] if triangle[i-1][j]<triangle[i-1][j-1] else triangle[i-1][j-1])
			if i == length-1 and (not ischange or triangle[i][j] < result):
				result = triangle[i][j]
				ischange = True
	return result

def minimumTotalV2(triangle):
	triangle = triangle[::-1]
	length = len(triangle)
	for i in range(1, length):
		li = len(triangle[i])
		for j in range(li):
			triangle[i][j] += (triangle[i-1][j] if triangle[i-1][j]<triangle[i-1][j+1] else triangle[i-1][j+1])
	return triangle[length-1][0] 


if __name__ == '__main__':
	li = [ [2], [3, 4], [6, 5, 7], [4, 1, 8, 3] ]
	li = [[-1],[2,3],[1,-1,-1]]
	print minimumTotalV2(li)
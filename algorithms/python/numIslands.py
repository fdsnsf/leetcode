
class Solution(object):
	"""docstring for Solution"""
	
	def numIslands(self, grid):
		if not grid:
			return 0
		result = 0
		y = len(grid)
		x = len(grid[0])
		tag = [[False]*x for k in range(y)]
		num = x*y
		while num:
			for i in range(x):
				for j in range(y):
					if not tag[i][j] and grid[i][j] == '1':


		return result


s = Solution()

c = ['111','010', '111']
print s.numIslands(c)

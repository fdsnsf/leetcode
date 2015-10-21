
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
    1
  2   5
 3 4    6

    1
   2 5
    3 6
     4
     1 
       2
      3

"""

class Solution(object):

    def flatten(self, root):
    	if root == None:
    		return    		
    	right = root.right
    	if root.left != None:
    		self.flatten(root.left)
    		a = root.left
    		while a != None and a.right != None:
    			a = a.right
    		a.right = root.right
    		root.right = root.left
    		root.left = None
    	self.flatten(right)
    	return root

    def flatten2(self, root):
	    if not root:
	    	return
	    right = root.right
	    if root.left:
	    	#print root.val
	        self.flatten2(root.left)
	        leaf = root.left
	        while leaf.right:
	            leaf = leaf.right
	        root.right, root.left, leaf.right = root.left, None, root.right
	    self.flatten2(right)
	    return root


root = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)
#root.left = node_2
root.right = node_2
node_2.left = node_3
#node_2.right = node_4
#node_5.right = node_6
#node_4.left = node_7

#root = TreeNode(0)

s = Solution()
root = s.flatten2(root)

#node_2.left.right = node_2.right
#node_2.right = node_2.left
#node_2.left = None

#root = root.left
while root != None:
	print root.val
	root = root.right
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None
		

class Solution(object):
	"""docstring for Solution"""
	def deleteDuplicates(self, head):
		"""
		"""

		result = head
		while head and head.next :
			last = head.val
			if last == head.next.val:
				head.next = head.next.next
			else:
			    head = head.next
		return result

	def deleteDuplicates2(self, head):
		pre = curr = head
		while curr:
			if pre.val != curr.val:
				pre.next = curr
				pre = curr
			else:
				pre.next = curr.next
			curr = curr.next
		return head

	def deleteNode(self, node):
		node.val = node.next.val
		node.next = node.next.next
		return node

s = Solution()

head = ListNode(1)
node_1 = ListNode(1)
node_2 = ListNode(1)
node_3 = ListNode(3)
node_4 = ListNode(3)

head.next = node_1
node_1.next = node_2
node_2.next = node_3
#node_3.next = node_4

r = s.deleteDuplicates2(head)
r = s.deleteNode(head)


while r :
	print r.val
	r = r.next
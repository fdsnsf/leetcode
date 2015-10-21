
class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, value):
		self.value = value
		self.next = None

class Solution(object):

	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		result = head = ListNode(0)
		carry = 0
		while l1 or l2 or carry:
			s = (l1.value if l1 else 0) + (l2.value if l2 else 0) + carry
			head.next = ListNode(s%10)
			carry = s/10

			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
			head = head.next
		return result.next

s = Solution()
listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode1.next = listNode2
listNode3 = ListNode(3)
listNode2.next = listNode3
l1 = ListNode(5)
#l1.next = listNode1
l2 = ListNode(5)
#l2.next = listNode2

result = s.addTwoNumbers(l1, l2)

while result:
	print result.value
	result = result.next

class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None

def removeNthFromEnd(head, n):
	a = head
	temp = []
	while a != None:
		temp.append(a.val)
		a = a.next
	del temp[n*-1]
	result = ListNode(0)
	rs = result
	for i in temp:
		result.next = ListNode(i)
		result = result.next
	return rs.next

def removeNthFromEndv2(head, n):
	a = head
	length = 0
	while a != None:
		length += 1
		a = a.next
	delpot = length - n
	if delpot == 0:
		return head.next
	a = head
	while  delpot-1 != 0:
		a = a.next
		delpot -= 1
	#a.val = a.next.val
	a.next = a.next.next
	return head


head = ListNode(1)
node2 = ListNode(2)
head.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4

result = removeNthFromEndv2(head, 1)
while result != None:
	print result.val
	result = result.next


		
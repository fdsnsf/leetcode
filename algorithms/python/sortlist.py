#! /usr/bin/python

class ListNode:
    def __init__(self, x):
        self.val=x
        self.next=None
    def length(self):
        if self == None:
            return 0
        length=1
        while self.next != None:
            length = length+1
            self.next = self.next.next
        return length

class Solution:
        def sortList2(self, head):
            if head==None or head.next==None:
                return head
            low=head
            fast=head.next
            while fast!=None and fast.next!=None:
                low=low.next
                fast=fast.next.next
            m=self.sortList2(low.next) 
            low.next=None
            n=self.sortList2(head)
            
            if n==None:
                return m
            if m==None:
                return n
            r=ListNode(-1)
            s=r
            while m!=None and n!=None:
                if m.val > n.val:
                    s.next=n
                    s=s.next
                    n=n.next
                else:
                    s.next=m
                    s=s.next
                    m=m.next
            if m!=None:
                s.next=m
            if n!=None:
                s.next=n
            return r.next
        def sortList(self, head):
            if head == None or head.next == None:
                return head
            
            l = ListNode(0)
            r = ListNode(0)
            left = l
            right = r
            a = head.val
            head=head.next
            while head != None :
                if head.val <= a:
                    left.next = head                   
                    left = left.next                    
                else:
                    right.next = head
                    right = right.next                
                head = head.next
            left.next,right.next = None, None
            m=self.sortList(l.next)
            n=self.sortList(r.next)
            o = m
            key = ListNode(a)
            if m==None:
                key.next = n
                return key
            while o.next != None:
                o=o.next
            o.next = key
            key.next = n
            return m
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

a = ListNode(0)
b=a
b.next = node1 
b = b.next
b.next = node2
b = b.next
b.next = node5
b = b.next
b.next = node4
b = b.next
b.next = node3


#while a.next != None:
#   print a.val
#   a.val = a.next.val
#   a.next = a.next.next
  

result = ListNode(0)

pp=[result]
print 'pp',len(pp)

s = Solution()
result.next = s.sortList2(a.next)
while result.next != None:
    result.val = result.next.val
    result.next = result.next.next
    print result.val

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
      b = set(A)
      del A[:]
      for i in b:
          A.append(i)
      return len(A)
    def remove2(self, A):
       # A.sort()
       # A=itertools.groupby(A)
        A=list(set(A))
        print A
        return len(A)
    def remove3(self,A):
        size = len(A)
        if size <= 1:
            return size
        i, insert_pos = 1, 1
        while i < size:
            if A[i] != A[i-1]:
                A[insert_pos] = A[i]
                insert_pos = insert_pos + 1
            i = i+1
        return insert_pos
    def remove4(self,A):
        if len(A)==0 or len(A)==1:
            return len(A)
        index = 0
        for i in list(set(A)).sort(key=A.index):
           A[index] = i
           index = index + 1
        return index
    def remove5(self,A):
       if len(A)==0 or len(A)==1:
           return len(A)
       index = 1
       for i in range(1,len(A)):
          if A[i] != A[index-1]:
               index = index + 1
               A[index-1] = A[i]
       return index
s=Solution()
#A=[1,1,1]
#print A
#print s.removeDuplicates(A)
#print s.remove2(A)

a=[1,2]
print s.remove5(a)
print a
a=[]
print s.remove5(a)
print a


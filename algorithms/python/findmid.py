class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lena,lenb = len(A),len(b)
        length = lena + lenb
        C = A + B
        if length == 1:
            return C[0]
        if length%2 == 1:
            mid1 = mid2 = length / 2
        else:
            mid2 = length/2
            mid1 = length/2-1
        if lena==0 or lenb==0:
            return float(C[mid1]+c[mid2])/2
        i=0
        j=i+lena
        while j<length :
            while C[i] < C[j] and i < lena and i+j-lena < mid2:
                i = i + 1
            if i<lena and i+j-lena == mid2:
                if mid1==mid2:
                    return c[i]
                else:
                    return float(C[i]+C[j])/2
            while C[j] < C[i] and j < lenb and i+j-lena < mid2:
                j = j + 1
            if j<lena and i+j-lena == mid2:
                if mid1=mid2:
                    return c[j]
                else:
                    return float(C[i]+C[j])/2
a=[1,2,3]
b=[4,5,6]
s=Solution()
s.findMedianSortedArrays(a,b)

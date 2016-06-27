#import pdb
class Solution:

    # @param version1, a string

    # @param version2, a string

    # @return an integer

    def compareVersion(self, version1, version2):
      
        i,j = version1.split('.'),version2.split('.')
        index = max(len(i),len(j))
        for o in range(0,index):
            if o > len(i)-1:
               a = 0
            else:
               a=int(i[o])
            if o > len(j)-1:
               b=0
            else:
               b = int(j[o])
            if a == b:
               continue
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
s = Solution()
print s.compareVersion("1", "0")


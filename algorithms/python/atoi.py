import sys
import string
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        
        str = str.strip()

        sign = 1
        if len(str)>0:
            if str[0]=='+':
                str = str[1::]
            elif str[0] == '-':
                sign = -1
                str = str[1::]
       
        s = 0
        digital = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for i in str:
            if i>='0' and i<='9':
                s = s*10 + digital[i] 
            else:
                break
        
        
        result = sign * s
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result
        
        #return string.atoi(str)

s = Solution()
#print sys.argv[1]
#print s.myAtoi(sys.argv[1])

print '-1  --',s.myAtoi('-1')
print '+1  --',s.myAtoi('+1')
print '+-1  --',s.myAtoi('+-1')
print '   12  --',s.myAtoi('    12')
print '-1o89  --',s.myAtoi('-1o89')
print '  60kj7  --',s.myAtoi('   60kj7')
print '  -1ls2  --',s.myAtoi('   -1ls2')
print '1+  --',s.myAtoi('1+')
print '   1l23  --',s.myAtoi('   1l23')
print '-a  --',s.myAtoi('-a')
print '   -00012a12  --',s.myAtoi('    -00012a12')
print '2147483648',s.myAtoi('2147483648')
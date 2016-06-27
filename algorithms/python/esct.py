#! /usr/bin/python

class Solution:
    # @return a string
    def convertToTitle(self, num):
        r=''
        n=1
        s=(num-1)/26
        while num>26:
            if s>26:
                n+=1
                s=s/26
                continue
            r+=chr(ord('A')+s-1)
            num-=26**n*s
            s=(num-1)/26
            n=1
        if num != 0:
            r+=chr(ord('A')+num-1)
        return r
    def convertToTitle2(self, num):
        r=''
        while (num-1)/26 != 0:
            r+=chr(ord('A')+(num-1)%26)
            num = (num-1)/26
        r+=chr(ord('A')+num-1)
        return r[::-1]
    def largestNumber(self, num):
        if len(num)==1:
            return str(num[0])
        r=''
        #s=[str(i) for i in num]
        #s=sorted(s,reverse=True)
        print num 
        for i in range(1,len(num)):
            t=num[i]
            for j in range(i,-1,-1):
                if self.compare(str(t),str(num[j-1]))>0:
                    num[j]=num[j-1]
                else:
                    break
         
            num[j]=t  
        for s in range(len(num)):
            r+=str(num[s])
        return r
    def compare(self,s1,s2):
        if int(s1+s2)>int(s2+s1):
            return 1
        else:
            return 0
    def largestNumber2(self, num):
        print num
        print num.sort(cmp=self.compare2)
        print num
        r=''
        for i in range(len(num)-1,-1,-1):
            r+=str(num[i])
        return str(int(r))
    
    def compare2(self,s1,s2):
        if int(str(s1)+str(s2)) > int(str(s2)+str(s1)):
            return 1
        else:
            return -1
    def countAndSay(self, n):
        r=''
        s=str(n)
        count=1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                r+=str(count)
                r+=s[i-1]
                count=1
            else:
                count+=1
        r+=str(count)
        r+=s[i]
        return r
    def countAndSay2(self,n):
        r='1'
        i=0
        j=0
        for i in range(1,n):
            s=r
            r=''
            count=1
            for j in range(1,len(s)):
                if s[j]!=s[j-1]:
                    r+=str(count)
                    r+=s[j-1]
                    count=1
                else:
                    count+=1
            r+=str(count)
            r+=s[j]
        return r
    def pow(self, x, n):
        if n==0:
            return 1
        r=x
        for i in range(n):
            r*=x
        return r
s=Solution()
print s.pow(5,0)
print s.pow(0.2,3)
#print s.pow(0.00001,2147483647)
#print s.countAndSay2(1)
#print s.countAndSay2(2)
#print s.countAndSay2(7)
#while True:
    #print s.convertToTitle2(int(raw_input("input:")))
#print s.largestNumber([123,2,5,321])
#print s.largestNumber([121,12])
#print s.largestNumber([128,12])
#print s.largestNumber2([1,2])
#print s.largestNumber2([2,1])
#print s.largestNumber([1,2,4,8,16,32,64,128,256,512])
#print s.largestNumber([74,21,33,51,77,51,90,60,5,56])
#print s.largestNumber([4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398])

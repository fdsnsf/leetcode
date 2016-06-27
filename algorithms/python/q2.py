class Solution:

    # @param version1, a string

    # @param version2, a string

    # @return an integer

    def compareVersion(self, version1, version2):
        i,j = version1.split('.'),version2.split('.')
        
        if len(i) > len(j):
            appendlist(j, len(i) - len(j))
        elif len(i) < len (j):
            appendlist(i, len(j) - len(i))
        for a,b in zip(i,j):
            a,b = int(a),int(b)
            if a > b:
                return 1
            elif a < b:
                return -1

        return 0

    def appendlist(self, version, count):

        for i in range(0, count):

            version.append(0)

        return version

s = Solution()
s.compareVersion("0","1")

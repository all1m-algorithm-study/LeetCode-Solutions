# can remove adjacent char pairs

# return: the string after being good

# check
# empty string is also good
# 1 <= length <= 100

# recursion until s becomes good

class Solution:
    def makeGood(self, s):
        if len(s) <= 1: return s
        for i in range(len(s)-1):
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                return self.makeGood(s[:i] + s[i+2:])
        return s
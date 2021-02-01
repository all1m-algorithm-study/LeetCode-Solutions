class Solution:
    def myPow(self, x,n):
        ans = x**n
        if abs(ans) <= 10**4:
            return ans
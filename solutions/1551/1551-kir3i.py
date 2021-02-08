class Solution:
    def minOperations(self, n):
        return n*(n//2) - (n//2) * (n//2)
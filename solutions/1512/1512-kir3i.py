class Solution:
    def numIdenticalPairs(self, nums):
        cnts = [0] * 101
        for x in nums:
            cnts[x] += 1

        ans = 0
        for cnt in cnts:
            if cnt > 1:
                ans += self.nC2(cnt)
        return ans

    def nC2(self, n):
        return n*(n-1)//2
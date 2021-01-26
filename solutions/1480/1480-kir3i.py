class Solution:
    def runningSum(self, nums):
        ans = []
        ss = 0
        for x in nums:
            ss += x
            ans.append(ss)
        return ans
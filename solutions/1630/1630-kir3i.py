class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        return [self.isArithmetic(nums[lo:hi+1]) for lo, hi in zip(l, r)]

    def isArithmetic(self, nums):
        maxn = max(nums)
        minn = min(nums)
        if maxn == minn:
            return True

        jump = (maxn - minn) // (len(nums) - 1)
        if jump == 0:
            return False
        setNums = set(nums)
        for x in range(minn, maxn + 1, jump):
            if x not in setNums:
                return False
        return True
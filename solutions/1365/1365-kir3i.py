class Solution:
    def smallerNumbersThanCurrent(self, nums):
        cnt = {}
        for i, x in enumerate(sorted(nums)):
            if x not in cnt:
                cnt[x] = i

        return [cnt[x] for x in nums]

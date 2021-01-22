class Solution:
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.extend([nums[i], nums[n+i]])
        return ans
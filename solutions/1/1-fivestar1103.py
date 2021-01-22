class Solution(object):
    def twoSum(self, nums, target):
        myMap = {j: i for (i, j) in enumerate(nums)}
        for i in range(len(nums)):
            if (target - nums[i]) in myMap and i != myMap[target - nums[i]]:
                return [i, myMap[target - nums[i]]]

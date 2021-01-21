class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        myMap, i = {i: None for i in nums}, 1
        while True:
            if i not in myMap:
                return i
            i += 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 1:
            return TreeNode(nums[0])

        m = max(nums)

        if m == nums[0]:
            return TreeNode(m, right=self.constructMaximumBinaryTree(nums[1:]))
        elif m == nums[-1]:
            return TreeNode(m, left=self.constructMaximumBinaryTree(nums[:-1]))
        else:
            mi = nums.index(m)
            return TreeNode(m, left=self.constructMaximumBinaryTree(nums[:mi]),
                            right=self.constructMaximumBinaryTree(nums[mi+1:]))
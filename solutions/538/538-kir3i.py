# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root):
        self.updateVal(root, 0)
        return root

    def updateVal(self, node, sum):
        if not node:
            return 0

        if node.right:
            sum = self.updateVal(node.right, sum)

        sum += node.val
        node.val = sum

        if node.left:
            sum = self.updateVal(node.left, sum)

        return sum

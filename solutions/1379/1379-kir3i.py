# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        q = []
        q.append(cloned)

        while q:
            curr = q.pop()
            if curr.val == target.val:
                return curr

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
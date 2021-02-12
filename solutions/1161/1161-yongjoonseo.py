# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque([root])
        ri, rmx = 0, -float('inf')
        cnt = 0
        while q:
            cnt += 1
            tempsum = 0
            for _ in range(len(q)):
                node = q.popleft()
                tempsum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if rmx < tempsum:
                ri, rmx = cnt, tempsum
        return ri
        
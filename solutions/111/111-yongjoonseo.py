# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque([root])
        cnt = 0
        while q:
            cnt += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left or node.right:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                else:
                    return cnt
        
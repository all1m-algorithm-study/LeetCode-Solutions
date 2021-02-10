# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return
        q = deque([root])
        result = []
        while q:
            added = False
            for _ in range(len(q)):
                node = q.popleft()
                if not added:
                    added = True
                    result.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return result
        
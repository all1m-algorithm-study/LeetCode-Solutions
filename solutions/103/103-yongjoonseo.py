# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return
        q = deque()
        q.append(root)
        result = []
        toggle = 0
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if toggle: temp.reverse()
            toggle ^= 1
            result.append(temp)
        return result
        
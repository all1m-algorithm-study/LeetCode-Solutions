# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def deepestLeavesSum(self, root):
        lvSum = 0
        q = deque()
        q.append(root)
        qsz = 1

        while q:
            lvSum = 0
            for _ in range(qsz):
                curr = q.popleft()
                lvSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            qsz = len(q)
        return lvSum


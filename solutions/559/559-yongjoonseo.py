"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def BFS(self, root):
        q = deque([root])
        cnt = 0
        while q:
            cnt += 1
            for _ in range(len(q)):
                node = q.popleft()
                q.extend(node.children)
        return cnt
        
    def maxDepth(self, root: 'Node') -> int:
        if root == None: return 0
        return self.BFS(root)     
        
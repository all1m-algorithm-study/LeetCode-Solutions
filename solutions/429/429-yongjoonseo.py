"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return
        q = deque([root])
        result = []
        result.append([root.val])
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.children:
                    for child in node.children:
                        temp.append(child.val)
                        q.append(child)
            if temp: result.append(temp)
        return result
        
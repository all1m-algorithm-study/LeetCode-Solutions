# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root):
        ans = 0

        #BFS
        q = [(root, False)]
        while q:
            curr, isParentEven = q.pop()

            if curr.left:
                q.append((curr.left, curr.val % 2 == 0))
                if isParentEven:
                    ans += curr.left.val
            if curr.right:
                q.append((curr.right, curr.val % 2 == 0))
                if isParentEven:
                    ans += curr.right.val
        return ans

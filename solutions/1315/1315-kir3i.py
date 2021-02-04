# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root):
        ans = 0

        #DFS
        s = [(root, False)]
        while s:
            curr, isParentEven = s.pop()

            if curr.left:
                s.append((curr.left, curr.val % 2 == 0))
                if isParentEven:
                    ans += curr.left.val
            if curr.right:
                s.append((curr.right, curr.val % 2 == 0))
                if isParentEven:
                    ans += curr.right.val
        return ans

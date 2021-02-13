# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root):
        vals = []
        self.popNode(root, vals)
        return self.makeTree(0, len(vals)-1, vals)

    def makeTree(self, lo, hi, vals):
        if lo > hi:
            return None
        elif lo == hi:
            return TreeNode(vals[lo])
        mid = (lo + hi) // 2
        root = TreeNode(vals[mid])
        root.left = self.makeTree(lo, mid-1, vals)
        root.right = self.makeTree(mid+1, hi, vals)

        return root

    def popNode(self, root, res):
        if root.left:
            self.popNode(root.left, res)
        res.append(root.val)
        if root.right:
            self.popNode(root.right, res)

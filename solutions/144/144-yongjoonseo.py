# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        result = []
        result.append(root.val)
        if root.left: result.extend(self.preorderTraversal(root.left))
        if root.right: result.extend(self.preorderTraversal(root.right))
        return result
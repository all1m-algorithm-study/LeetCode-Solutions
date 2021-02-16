# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        result = []
        if root.left: result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        if root.right: result.extend(self.inorderTraversal(root.right))
        return result
        
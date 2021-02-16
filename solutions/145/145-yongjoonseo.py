# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        result = []
        if root.left: result.extend(self.postorderTraversal(root.left))
        if root.right: result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result
        
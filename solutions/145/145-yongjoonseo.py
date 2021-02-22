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
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        result.reverse()
        return result
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    def __init__(self, root):
        self.s = set([])
        self.setVal(root, 0)
    def setVal(self, node, val):
        if not node:
            return
        node.val = val
        self.s.add(val)
        self.setVal(node.left, 2*val+1)
        self.setVal(node.right, 2*val+2)

    def find(self, target):
        if target in self.s:
            return True
        else:
            return False
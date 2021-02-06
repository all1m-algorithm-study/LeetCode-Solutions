# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        ans = []
        t1 = []
        t2 = []
        self.popAscList(root1, t1)
        self.popAscList(root2, t2)
        
        i1 = i2 = 0

        while i1<len(t1) and i2<len(t2):
            if t1[i1] <= t2[i2]:
                ans.append(t1[i1])
                i1 += 1
            else:
                ans.append(t2[i2])
                i2 += 1
        if i1 == len(t1):
            ans.extend(t2[i2:])
        else:
            ans.extend(t1[i1:])
        return ans
    
    def popAscList(self, root, res):
        if not root:
            res = []
            return
        
        if root.left:
            self.popAscList(root.left, res)
        res.append(root.val)
        if root.right:
            self.popAscList(root.right, res)
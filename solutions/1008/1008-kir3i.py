class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        for n in preorder[1:]:
            self.pushNode(root, TreeNode(n))
        return root

    def pushNode(self, root, child):
        print(f'{child.val} push in {root.val}')
        if child.val < root.val:
            if root.left:
                self.pushNode(root.left, child)
            else:
                root.left = child
        else:
            if root.right:
                self.pushNode(root.right, child)
            else:
                root.right = child
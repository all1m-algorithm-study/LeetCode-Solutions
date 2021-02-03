/* Definition for a binary tree node. 
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
*/
class Solution {
public:
	TreeNode* bstFromPreorder(vector<int>& preorder) {
		int sz = preorder.size();
		TreeNode *root = new TreeNode(preorder[0]);
		for (int i = 1; i < sz; i++) {
			pushNode(root, new TreeNode(preorder[i]));
		}

		return root;
	}

	void pushNode(TreeNode *root, TreeNode *child) {
		if (child->val < root->val)
			if (root->left)	pushNode(root->left, child);
			else   root->left = child;
		else
			if (root->right) pushNode(root->right, child); 
			else	root->right = child;
	}
};
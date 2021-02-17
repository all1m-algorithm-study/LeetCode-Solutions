/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> vals;
    TreeNode* balanceBST(TreeNode* root) {
        popNode(root);
        return makeTree(0, vals.size() - 1);
    }
    
    TreeNode* makeTree(int lo, int hi) {
        if (lo > hi)        return nullptr;
        else if (lo == hi)  return new TreeNode(vals[lo]);
        
        int mid = (lo + hi) / 2;
        TreeNode* root = new TreeNode(vals[mid]);
        root->left = makeTree(lo, mid - 1);
        root->right = makeTree(mid + 1, hi);
        return root;
    }
    
    void popNode(TreeNode *root) {
        if(!root)   return;
        popNode(root->left);
        vals.push_back(root->val);
        popNode(root->right);
    }
};

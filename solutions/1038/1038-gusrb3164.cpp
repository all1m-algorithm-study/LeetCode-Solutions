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
class Solution
{
public:
    int maxVal = 0;
    TreeNode *bstToGst(TreeNode *root)
    {
        dfs(root);
        return root;
    }
    void dfs(TreeNode *node)
    {
        if (node == nullptr)
            return;

        dfs(node->right);
        maxVal += node->val;
        node->val = maxVal;
        dfs(node->left);
    }
};
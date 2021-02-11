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
    TreeNode *invertTree(TreeNode *root)
    {
        dfs(root);
        return root;
    }
    TreeNode *dfs(TreeNode *node)
    {
        if (node == nullptr)
            return nullptr;

        TreeNode *left = dfs(node->left);
        TreeNode *right = dfs(node->right);
        node->right = left;
        node->left = right;
        return node;
    }
};
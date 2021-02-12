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
    int result = 123456789;
    int prev = -result;

public:
    int minDiffInBST(TreeNode *root)
    {
        dfs(root);
        return result;
    }
    void dfs(TreeNode *node)
    {
        if (node->left != nullptr)
        {
            dfs(node->left);
        }
        result = min(result, node->val - prev);
        prev = node->val;
        if (node->right != nullptr)
        {
            dfs(node->right);
        }
    }
};
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
    bool isBalanced(TreeNode *root)
    {
        if (dfs(root) == -1)
            return false;
        return true;
    }
    int dfs(TreeNode *node)
    {
        if (node == nullptr)
        {
            return 0;
        }
        int leftDepth = dfs(node->left);
        int rightDepth = dfs(node->right);
        if (leftDepth == -1 || rightDepth == -1 || abs(leftDepth - rightDepth) > 1)
        {
            return -1;
        }
        else
        {
            return max(leftDepth, rightDepth) + 1;
        }
    }
};
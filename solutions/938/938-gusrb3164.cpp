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
    int sum = 0;
    int low, high;
    int rangeSumBST(TreeNode *root, int low, int high)
    {
        this->low = low;
        this->high = high;
        dfs(root);
        return sum;
    }
    void dfs(TreeNode *node)
    {
        if (node == nullptr)
            return;
        if (low <= node->val && node->val <= high)
        {
            sum += node->val;
            dfs(node->right);
            dfs(node->left);
        }
        else if (node->val < low)
        {
            dfs(node->right);
        }
        else
        {
            dfs(node->left);
        }
    }
};
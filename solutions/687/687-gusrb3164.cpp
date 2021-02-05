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
    int result = 0;

public:
    int longestUnivaluePath(TreeNode *root)
    {
        dfs(root);
        return result;
    }
    int dfs(TreeNode *cur)
    {
        if (cur == nullptr)
        {
            return 0;
        }
        int left = dfs(cur->left);
        int right = dfs(cur->right);
        if (cur->left != nullptr && cur->val == cur->left->val)
        {
            left++;
        }
        else
        {
            left = 0;
        }
        if (cur->right != nullptr && cur->val == cur->right->val)
        {
            right++;
        }
        else
        {
            right = 0;
        }
        result = max(result, left + right);
        return max(left, right);
    }
};
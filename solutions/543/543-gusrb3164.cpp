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
    int result = 0;
    int diameterOfBinaryTree(TreeNode *root)
    {
        dfs(root);
        return result;
    }
    int dfs(TreeNode *cur)
    {
        if (cur == nullptr)
            return -1;
        int left = dfs(cur->left);
        int right = dfs(cur->right);
        int curMax = left + right + 2;
        result = max(result, curMax);
        return max(left, right) + 1;
    }
};
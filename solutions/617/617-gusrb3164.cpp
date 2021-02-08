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
    TreeNode *mergeTrees(TreeNode *root1, TreeNode *root2)
    {
        TreeNode *root = dfs(root1, root2);
        return root;
    }
    TreeNode *dfs(TreeNode *node1, TreeNode *node2)
    {
        if (node1 == nullptr && node2 == nullptr)
            return nullptr;
        else if (node1 == nullptr)
        {
            return node2;
        }
        else if (node2 == nullptr)
        {
            return node1;
        }
        else
        {
            TreeNode *left = dfs(node1->left, node2->left);
            TreeNode *right = dfs(node1->right, node2->right);
            TreeNode *cur = new TreeNode();
            cur->val = node1->val + node2->val;
            cur->left = left;
            cur->right = right;
            return cur;
        }
    }
};
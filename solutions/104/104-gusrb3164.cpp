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
    int maxDepth(TreeNode *root)
    {
        if (root == nullptr)
        {
            return 0;
        }
        queue<TreeNode> q;
        q.push(*root);
        int result = 0;
        while (!q.empty())
        {
            result++;
            int len = q.size();
            for (int i = 0; i < len; i++)
            {
                TreeNode tmp = q.front();
                q.pop();
                if (tmp.left != nullptr)
                {
                    q.push(*tmp.left);
                }
                if (tmp.right != nullptr)
                {
                    q.push(*tmp.right);
                }
            }
        }
        return result;
    }
};
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
    vector<int> iorder;
    vector<int> porder;

    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        iorder = inorder;
        porder = preorder; // 전역 변수로 재정의

        return dfs(0, iorder.size() - 1);
    }
    TreeNode *dfs(int start, int end)
    {
        if (start > end || porder.empty())
            return nullptr;
        int idx = findIdx(porder[0]); //현재 루트값이 inorder에서 위치한 인덱스 저장
        porder.erase(porder.begin());

        TreeNode *node = new TreeNode(iorder[idx]);

        node->left = dfs(start, idx - 1);
        node->right = dfs(idx + 1, end);
        return node;
    }
    int findIdx(int num)
    {
        for (int i = 0; i < iorder.size(); i++)
        {
            if (iorder[i] == num)
                return i;
        }
        return -1;
    }
};
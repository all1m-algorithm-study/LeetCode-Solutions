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
class Solution {
public:
    vector<int> ans, t1, t2;
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        int i1=0, i2=0;
        popAscList(root1, t1);
        popAscList(root2, t2);
        
        while(i1<t1.size() && i2<t2.size()) {
            if (t1[i1] <= t2[i2])
                ans.push_back(t1[i1++]);
            else
                ans.push_back(t2[i2++]);
        }
        
        if (i1 == t1.size())
            ans.insert(ans.end(), t2.begin()+i2, t2.end());
        else
            ans.insert(ans.end(), t1.begin()+i1, t1.end());
        
        return ans;
    }
    
    void popAscList(TreeNode* root, vector<int> &t) {
        if (!root) {
            t = {};
            return;
        }
        
        if (root->left)
            popAscList(root->left, t);
        t.push_back(root->val);
        if (root->right)
            popAscList(root->right, t);
    }
};
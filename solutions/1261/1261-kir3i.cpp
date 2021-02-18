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
class FindElements {
public:
    unordered_set<int> s;
    FindElements(TreeNode* root) {
        setVal(root, 0);
    }
    
    void setVal(TreeNode *node, const int &val) {
        if(!node)   return;
        node->val = val;
        s.insert(val);
        setVal(node->left, 2*val+1);
        setVal(node->right, 2*val+2);
    }
    
    bool find(int target) {
        return s.find(target) != s.end();
    }
};

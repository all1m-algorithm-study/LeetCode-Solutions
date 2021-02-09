/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#define INF 200000
class Codec
{
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode *root)
    {
        queue<TreeNode *> q;
        string result = "";
        q.push(root);
        while (!q.empty())
        {
            TreeNode *cur = q.front();
            q.pop();
            if (cur == nullptr)
            {
                result += "# ";
            }
            else
            {
                result += (to_string(cur->val) + " ");
                q.push(cur->left);
                q.push(cur->right);
            }
        }
        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data)
    {
        if (data == "" || data[0] == '#')
        {
            return nullptr;
        }
        // cout<<data<<endl;
        vector<TreeNode *> nums;
        stringstream ss(data);
        string temp;

        while (getline(ss, temp, ' '))
        {
            if (temp == "#")
            {
                nums.push_back(nullptr);
            }
            else
            {
                nums.push_back(new TreeNode(stoi(temp)));
            }
        }

        TreeNode *result = nums[0];
        queue<TreeNode *> q;
        q.push(result);
        int idx = 0;
        while (!q.empty())
        {
            TreeNode *node = q.front();
            q.pop();

            idx++;
            if (nums[idx])
            {
                node->left = nums[idx];
                q.push(node->left);
            }

            idx++;
            if (nums[idx])
            {
                node->right = nums[idx];
                q.push(node->right);
            }
        }
        return result;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
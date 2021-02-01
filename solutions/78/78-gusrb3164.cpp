class Solution
{
public:
    vector<vector<int>> result;
    vector<vector<int>> subsets(vector<int> &nums)
    {
        vector<int> tmp;
        result.push_back(tmp);
        dfs(nums, tmp, 0);
        return result;
    }
    void dfs(vector<int> &nums, vector<int> cur, int start)
    {
        if (start >= nums.size())
            return;
        for (int i = start; i < nums.size(); i++)
        {
            vector<int> tmp = cur;
            tmp.push_back(nums[i]);
            result.push_back(tmp);
            dfs(nums, tmp, i + 1);
        }
    }
};
class Solution
{
public:
    vector<vector<int>> result;
    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {
        for (int i = 0; i < candidates.size(); i++)
        {
            vector<int> current;
            dfs(i, target, current, candidates);
        }
        return result;
    }
    void dfs(int start, int sum, vector<int> current, vector<int> &candidates)
    {
        sum -= candidates[start];
        current.push_back(candidates[start]);
        if (sum < 0)
            return;
        else if (sum == 0)
        {
            result.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size(); i++)
        {
            dfs(i, sum, current, candidates);
        }
    }
};
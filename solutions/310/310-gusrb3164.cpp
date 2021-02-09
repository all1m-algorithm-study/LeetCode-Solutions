class Solution
{
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges)
    {
        if (n <= 1)
            return {0};
        vector<vector<int>> graph(n);

        for (auto &edge : edges)
        {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        vector<int> leaves;
        for (int i = 0; i < n; i++)
        {
            if (graph[i].size() == 1)
            {
                leaves.push_back(i);
            }
        }
        while (n > 2)
        {
            n -= leaves.size();
            vector<int> newLeaves;
            //i = 해당 n
            for (auto leaf : leaves)
            {
                int next = graph[leaf][0];
                rmNum(graph[next], leaf);
                if (graph[next].size() == 1)
                {
                    newLeaves.push_back(next);
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
    //벡터내의 특정 값 지우는 함수
    void rmNum(vector<int> &nums, int num)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == num)
            {
                nums.erase(nums.begin() + i);
                return;
            }
        }
    }
};
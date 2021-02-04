class Solution
{
public:
    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> road;
    vector<string> result;
    vector<string> findItinerary(vector<vector<string>> &tickets)
    {
        // 각 키에 우선순위 큐를 이용해 자동 정렬
        for (auto i : tickets)
        {
            road[i[0]].push(i[1]);
        }

        dfs("JFK");

        reverse(result.begin(), result.end());
        return result;
    }
    //백트래킹
    void dfs(string cur)
    {
        while (!road[cur].empty())
        {
            string next = road[cur].top();
            road[cur].pop();
            dfs(next);
        }
        result.push_back(cur);
    }
};
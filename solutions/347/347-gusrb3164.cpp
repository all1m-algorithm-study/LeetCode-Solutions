class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> um;
        vector<int> result;
        priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq;

        for (auto i : nums)
        {
            um[i]++;
        }

        for (auto i : um)
        {
            pq.push(make_pair(i.second, i.first));
        }
        for (int i = 0; i < k; i++)
        {
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};
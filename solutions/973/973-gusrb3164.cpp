class Solution
{
public:
    vector<vector<int>> kClosest(vector<vector<int>> &points, int K)
    {
        priority_queue<vector<int>, vector<vector<int>>, comp> pq;
        vector<vector<int>> result;
        for (auto i : points)
        {
            pq.push(i);
        }
        for (int i = 0; i < K; i++)
        {
            result.push_back(pq.top());
            pq.pop();
        }
        return result;
    }
    struct comp
    {
        bool operator()(vector<int> a, vector<int> b)
        {
            int powA = a[0] * a[0] + a[1] * a[1];
            int powB = b[0] * b[0] + b[1] * b[1];
            return powA > powB;
        }
    };
};
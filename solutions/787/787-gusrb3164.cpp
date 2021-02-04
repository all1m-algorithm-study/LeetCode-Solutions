class Solution
{
public:
    int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst, int K)
    {
        //배열 각각에 다음 노드, price가 있음
        vector<vector<pair<int, int>>> graph(n);
        for (auto &i : flights)
        {
            graph[i[0]].push_back(make_pair(i[1], i[2]));
        }
        //해당 노드까지의 price, 노드, 남은 경유지 수 순서로 큐를 구성
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        pq.push({0, src, K});
        while (!pq.empty())
        {
            int price = pq.top()[0];
            int node = pq.top()[1];
            int rest = pq.top()[2];
            pq.pop();
            if (node == dst)
            {
                return price;
            }
            if (rest >= 0)
            {
                for (auto i : graph[node])
                {
                    pq.push({price + i.second, i.first, rest - 1});
                }
            }
        }
        return -1;
    }
};
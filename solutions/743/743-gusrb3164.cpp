#define MAX 123456789
class Solution
{
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k)
    {
        //(연결노드, 시간)
        vector<vector<pair<int, int>>> graph(n + 1);
        //우선순위 큐
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> load;
        //각 노드별 최단 거리
        vector<int> currentCost(n + 1, MAX);
        int result = 0;

        for (auto i : times)
        {
            graph[i[0]].push_back(make_pair(i[1], i[2]));
        }
        load.push(make_pair(0, k));
        while (!load.empty())
        {
            int time = load.top().first;
            int node = load.top().second;
            load.pop();
            //이미 작은 값이 존재하면 continue
            if (currentCost[node] <= time)
            {
                continue;
            }
            //최소값을 갱신하고 이어진 다음 노드 탐색
            currentCost[node] = time;
            for (auto i : graph[node])
            {
                int nextNode = i.first;
                int nextTime = i.second + time;
                if (nextTime < currentCost[nextNode])
                {
                    load.push(make_pair(nextTime, nextNode));
                }
            }
        }
        //최장 시간을 찾는데 방문 안한 곳이 있으면 -1 반환
        result = *max_element(currentCost.begin() + 1, currentCost.end());
        if (result == MAX)
            return -1;
        return result;
    }
};
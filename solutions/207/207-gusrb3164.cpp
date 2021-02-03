class Solution
{
public:
    unordered_map<int, bool> globalVisited; //해당 코스의 결과 기록
    unordered_set<int> visited;             // dfs 도는 내부 코스 방문 기록
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<vector<int>> pre(numCourses);

        for (int i = 0; i < prerequisites.size(); i++)
        {
            pre[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        for (auto i : prerequisites)
        {
            if (!dfs(i[0], pre))
                return false;
        }
        return true;
    }
    bool dfs(int cur, vector<vector<int>> &pre)
    {
        //이미 방문한 기록이 있는데 순환 구조면 false  비순환 구조면 true
        if (globalVisited.find(cur) != globalVisited.end() && globalVisited[cur] == false)
        {
            return false;
        }
        else if (globalVisited.find(cur) != globalVisited.end() && globalVisited[cur] == true)
        {
            return true;
        }
        if (visited.find(cur) != visited.end())
        {
            return false;
        }
        else
        {
            visited.insert(cur);
        }
        for (auto i : pre[cur])
        {
            if (!dfs(i, pre))
            {
                visited.erase(cur);
                globalVisited[cur] = false;
                return false;
            }
        }
        visited.erase(cur);
        globalVisited[cur] = true;
        return true;
    }
};
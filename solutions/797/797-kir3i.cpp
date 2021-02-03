class Solution {
public:
	vector<int> visitLog;
	vector<vector<int>> ans;
	int target;

	vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
		target = graph.size() - 1;
		dfs(graph, 0);
		return ans;
	}

	void dfs(vector<vector<int>> &graph, int curr) {
		visitLog.push_back(curr);
		if (curr == target)
			ans.push_back(vector<int>(visitLog));
		else
			for (int &nxt : graph[curr])
				dfs(graph, nxt);

		visitLog.pop_back();
	}
};

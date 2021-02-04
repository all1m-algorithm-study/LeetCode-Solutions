class Solution:
    def allPathsSourceTarget(self, graph):
        self.target = len(graph) - 1
        self.ans = []
        self.dfs(graph, 0)

        return self.ans

    def dfs(self, graph, curr, visitLog=[]):
        if curr == self.target:
            self.ans.append(visitLog+[curr])
            return

        for next in graph[curr]:
            print(f'{curr} -> {next}')
            print(visitLog)
            self.dfs(graph, next, visitLog+[curr])

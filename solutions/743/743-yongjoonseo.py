class Solution:
    def dijkstra(self, graph, n, k):
        dist = [float('inf')] * (n + 1)
        visited = [0] * (n + 1)
        dist[k] = 0
        for i in range(1, n+1):
            mi, mn = 0, float('inf')
            for j in range(1, n+1):
                if not visited[j] and mn > dist[j]:
                    mi, mn = j, dist[j]
            visited[mi] = 1
            if mi in graph:
                for e, val in graph.get(mi):
                    if not visited[e] and dist[e] > dist[mi] + val:
                        dist[e] = dist[mi] + val
        mx = -1
        for i in range(1, n+1):
            if dist[i] == float('inf'): return -1
            mx = max(mx, dist[i])
        return mx
        
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = dict()
        for u, v, w in times:
            if u in graph: graph[u].append((v, w))
            else: graph[u] = [(v, w)]
        return self.dijkstra(graph, n, k)
        
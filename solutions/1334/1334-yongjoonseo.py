class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for s, e, val in edges:
            dist[s][e] = val
            dist[e][s] = val
    
        for k in range(n):
            for i in range(n):
                if dist[i][k] != float('inf'):
                    for j in range(i):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                        dist[j][i] = dist[i][j]
    
        result, resval = -1, 101
        for i in range(-1, -n-1, -1):
            cnt = 0
            for j in range(n):
                if n+i == j or dist[i][j] == float('inf'): continue
                if dist[i][j] <= distanceThreshold: cnt += 1
            if resval > cnt:
                result, resval = n+i, cnt
        return result
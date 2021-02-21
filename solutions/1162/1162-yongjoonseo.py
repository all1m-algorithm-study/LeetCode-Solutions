from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        water_cnt = 0
        q = deque()
        visited = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]: 
                    q.append((i, j))
                    visited[i][j] = 1
                else:
                    water_cnt += 1
        if water_cnt in (0, n ** 2): return -1
        
        step = -1
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        while q:
            step += 1
            for _ in range(len(q)):
                y, x = q.popleft()
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and not grid[ny][nx]:
                        visited[ny][nx] = 1
                        q.append((ny, nx))
        return step
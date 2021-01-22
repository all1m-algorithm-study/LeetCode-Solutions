from collections import deque

class Solution:
    def BFS(self, visited, i, j, grid, m, n):
        q = deque([(i, j)])
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and grid[ny][nx] == '1':
                    visited[ny][nx] = 1
                    q.append((ny, nx))
        
    def numIslands(self, grid) -> int:
        visited = [[0] * len(grid[0]) for i in range(len(grid))]
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = 1
                    self.BFS(visited, i, j, grid, m, n)
                    cnt += 1
        return cnt
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for i in range(m)]
        q = deque()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited[i][j] = 1
                    q.append((i, j))
                elif grid[i][j] == 1: cnt += 1
        time = 0
        while q:
            time += 1
            for _ in range(len(q)):
                y, x = q.popleft()
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and grid[ny][nx] == 1:
                        cnt -= 1
                        if not cnt: return time
                        visited[ny][nx] = 1
                        q.append((ny, nx))
        if cnt: return -1
        else: return 0
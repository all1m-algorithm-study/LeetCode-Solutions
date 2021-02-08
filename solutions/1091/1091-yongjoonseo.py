from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        q = deque([(0, 0)])
        n = len(grid)
        if n == 1:
            if grid[0][0] == 0: return 1
            else: return -1
        visited = [[0] * n for i in range(n)]
        visited[0][0] = 1
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        cnt = 1
        while q:
            cnt += 1
            for _ in range(len(q)):
                y, x = q.popleft()
                for i in range(8):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and not grid[ny][nx]:
                        if (ny, nx) == (n-1, n-1): return cnt
                        visited[ny][nx] = 1
                        q.append((ny, nx))
        return -1
        
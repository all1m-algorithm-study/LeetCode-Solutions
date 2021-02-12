from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        visited = [[0] * m for i in range(n)]
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        q = deque()
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]: 
                    q.append((i, j))
                    visited[i][j] = 1
        cnt = 0    
        while q:
            cnt += 1
            for _ in range(len(q)):
                y, x = q.popleft()
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        matrix[ny][nx] = cnt
                        q.append((ny, nx))
        return matrix
        
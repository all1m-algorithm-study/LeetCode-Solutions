from collections import deque

class Solution:
    def BFS(self, board, sy, sx, visited, n, m):
        q = deque([(sy, sx)])
        visited[sy][sx] = 1
        candis = [(sy, sx)]
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        out = False
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and board[ny][nx] == 'O':
                        visited[ny][nx] = 1
                        candis.append((ny, nx))
                        q.append((ny, nx))
                else:
                    if not out: out = True
        if out: return
        for cy, cx in candis:
            board[cy][cx] = 'X'
                
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        n, m = len(board), len(board[0])
        visited = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    self.BFS(board, i, j, visited, n, m)
        
        
        
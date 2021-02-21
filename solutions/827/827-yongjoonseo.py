from collections import deque

class Solution:
    def find(self, coor, parents):
        y, x = coor
        if parents[y][x] == coor: return coor
        parents[y][x] = self.find(parents[y][x], parents)
        return parents[y][x]
    
    def union(self, coor1, coor2, parents, ranks):
        y1r, x1r = self.find(coor1, parents)
        y2r, x2r = self.find(coor2, parents)
        if ranks[y1r][x1r] >= ranks[y2r][x2r]:
            parents[y2r][x2r] = [y1r, x1r]
        else:
            parents[y1r][x1r] = [y2r, x2r]
        if ranks[y1r][x1r] == ranks[y2r][x2r]:
            ranks[y1r][x1r] += 1
    
    def BFS(self, grid, visited, coor, parents, ranks, dy, dx, n): # return cnt
        q = deque([coor])
        cnt = 1
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and grid[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    self.union((y, x), (ny, nx), parents, ranks)
                    cnt += 1
        return cnt
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        visited = [[0] * n for i in range(n)]
        parents = [[[i, j] for j in range(n)] for i in range(n)]
        ranks = [[0] * n for i in range(n)]
        zeros = []
        cnts = dict()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    visited[i][j] = 1
                    val = self.BFS(grid, visited, (i,j), parents, ranks, dy, dx, n)
                    cnts[(i, j)] = val
                else:
                    zeros.append((i, j))
        
        result = 0
        if zeros:
            for y, x in zeros:
                temp_cnt = 1
                checked = set()
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n:
                        coor = tuple(self.find((ny, nx), parents))
                        if coor in checked: continue
                        checked.add(coor)
                        if coor in cnts: temp_cnt += cnts.get(coor)
                result = max(result, temp_cnt)
        else:
            return cnts.get((0,0))
        return result
        
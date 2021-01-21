class Solution:
    def find(self, x, parents):
        if parents[x] == x: return x
        parents[x] = self.find(parents[x], parents)
        return parents[x]
    
    def union(self, x, y, parents, ranks):
        xr = self.find(x, parents)
        yr = self.find(y, parents)
        if ranks[xr] >= ranks[yr]:
            parents[yr] = xr
        else:
            parents[xr] = yr
        if ranks[xr] == ranks[yr]:
            ranks[xr] += 1
    
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        parents = [i for i in range(n)]
        ranks = [0] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    if self.find(i, parents) != self.find(j, parents):
                        self.union(i, j, parents, ranks)
        result = set()
        for ele in parents:
            result.add(self.find(ele, parents))
        return len(result)
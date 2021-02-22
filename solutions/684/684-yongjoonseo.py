# check
# return the answer that occurs last

class Solution:
    def find(self, x, parents):
        if parents[x] == x: return x
        parents[x] = self.find(parents[x], parents)
        return parents[x]
    
    def union(self, x, y, parents, ranks):
        xr = self.find(x, parents)
        yr = self.find(y, parents)
        if ranks[xr] >= ranks[yr]: parents[yr] = xr
        else: parents[xr] = yr
        if ranks[xr] == ranks[yr]: ranks[xr] += 1
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = [i for i in range(N+1)]
        ranks = [0] * (N+1)
        result = None
        for u, v in edges:
            if self.find(u, parents) == self.find(v, parents): result = (u, v)
            else: self.union(u, v, parents, ranks)
        return result
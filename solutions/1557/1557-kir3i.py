class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        ind = [0] * n
        for e in edges:
            ind[e[1]] += 1

        return [i for i, d in enumerate(ind) if d == 0]

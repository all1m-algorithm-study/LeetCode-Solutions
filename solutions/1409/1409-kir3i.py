class Solution:
    def processQueries(self, queries, m):
        ans = []
        perm = list(range(1, m+1))
        for q in queries:
            tar = perm.index(q)
            ans.append(tar)
            perm.pop(tar)
            perm.insert(0, q)
        return ans
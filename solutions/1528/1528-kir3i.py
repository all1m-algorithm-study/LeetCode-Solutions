class Solution:
    def restoreString(self, s, indices):
        ans = [''] * len(indices)
        for i, c in zip(indices, s):
            ans[i] = c
        return ''.join(ans)

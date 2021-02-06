class Solution:
    def numTeams(self, rating):
        ans = 0
        for i, x in enumerate(rating):
            if i == 0 or i == len(rating):
                continue
            Llen = i
            Rlen = len(rating) - i - 1
            Lbig = len([n for n in rating[:i] if n>x])
            Rbig = len([n for n in rating[i+1:] if n>x])
            ans += Lbig*(Rlen-Rbig) + Rbig*(Llen-Lbig)
        return ans

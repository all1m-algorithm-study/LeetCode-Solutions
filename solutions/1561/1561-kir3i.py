class Solution:
    def maxCoins(self, piles):
        return sum(sorted(piles, reverse=True)[1:2*len(piles)//3:2])

class Solution:
    def maximumWealth(self, accounts):
        return max([sum(account) for account in accounts])

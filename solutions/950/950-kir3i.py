from collections import deque as dq

class Solution:
    def deckRevealedIncreasing(self, deck):
        ans = dq([])
        for x in sorted(deck, reverse=True):
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(x)
        return list(ans)

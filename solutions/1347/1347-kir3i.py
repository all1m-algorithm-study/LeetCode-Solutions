class Solution:
    def minSteps(self, s, t):
        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
        ans = 0
        for c in t:
            if c in cnt and cnt[c] > 0:
                cnt[c] -= 1
            else:
                ans += 1
            
        return ans

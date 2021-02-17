class Solution:
    def decode(self, encoded, first):
        ans = [first]
        for x in encoded:
            ans.append(ans[-1]^x)
        return ans

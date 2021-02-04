class Solution:
    def partitionLabels(self, S):
        S = [ord(c) - 97 for c in S]
        le = [None] * 26
        re = [None] * 26

        # First Scan
        for i, x in enumerate(S):
            if le[x] == None:
                le[x] = i
            re[x] = i

        # Second Scan
        ans = []
        cnt = 0
        sp = 0
        for i, x in enumerate(S):
            if cnt == 0:
                sp = i
            if le[x] == i:
                cnt += 1
            if cnt == 1 and re[x] == i:
                ans.append(i-sp+1)
            if re[x] == i:
                cnt -= 1

        return ans

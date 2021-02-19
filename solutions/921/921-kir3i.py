class Solution:
    def minAddToMakeValid(self, S):
        openCnt = 0
        closeCnt = 0
        for c in S:
            if c == '(':
                openCnt += 1
            elif c == ')':
                if openCnt > 0:
                    openCnt -= 1
                else:
                    closeCnt += 1
        return openCnt+closeCnt

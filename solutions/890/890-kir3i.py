class Solution:
    def findAndReplacePattern(self, words, pattern):
        sz = len(pattern)
        ans = []
        for w in words:
            ok = True
            trans = {}
            used = set([])
            for i in range(sz):
                if pattern[i] not in trans:
                    if w[i] in used:
                        ok = False
                        break
                    trans[pattern[i]] = w[i]
                    used.add(w[i])
                elif trans[pattern[i]] != w[i]:
                    ok = False
                    break
            if ok:
               ans.append(w)
        return ans

class Solution:
    def countGoodRectangles(self, rectangles) -> int:
        s = dict()
        for x, y in rectangles:
            mv = min(x, y)
            if mv in s: s[mv] += 1
            else: s[mv] = 1
        return s.get(max(s.keys()))
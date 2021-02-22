# s <= ns
# 1. e <= ns: change
# 2. ns < e < ne: change
# => e < ne: change
# else: cnt += 1, don't change

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        s = e = -1
        cnt = 0
        for ns, ne in intervals:
            if e < ne:
                if s == ns: cnt += 1
                s, e = ns, ne
            else: cnt += 1
        return len(intervals) - cnt
        
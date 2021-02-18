class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        s, e = intervals[0]
        for i in range(1, len(intervals)):
            ns, ne = intervals[i]
            if ns > e:
                result.append([s, e])
                s, e = ns, ne
            else:
                if ne > e: e = ne
        result.append([s, e])
        return result
            
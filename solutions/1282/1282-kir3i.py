class Solution:
    def groupThePeople(self, groupSizes):
        match = {}
        for idx, groupSize in enumerate(groupSizes):
            if groupSize in match:
                match[groupSize].append(idx)
            else:
                match[groupSize] = [idx]

        ans = []
        for groupSize, m in match.items():
            while m:
                ans.append(m[:groupSize])
                m = m[groupSize:]
        
        return ans
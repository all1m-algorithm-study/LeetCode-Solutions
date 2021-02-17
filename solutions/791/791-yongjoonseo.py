# check
# lowercase letters

# count all the letters of T which S contains
# save indices of letters in T

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        result = [0] * len(T)
        indices = []
        counts = dict()
        for i in range(len(T)):
            if T[i] in S:
                indices.append(i)
                if T[i] in counts: counts[T[i]] += 1
                else: counts[T[i]] = 1
            else:
                result[i] = T[i]
        i = 0
        for char in S:
            left = counts.get(char)
            while left:
                result[indices[i]] = char
                i += 1
                left -= 1
        return ''.join(result)
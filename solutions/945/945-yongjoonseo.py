from collections import deque

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        check = [0] * 80000
        rest = deque()
        for num in A:
            if not check[num]: check[num] = 1
            else: rest.append(num)
        result = 0
        i = 0
        while rest:
            num = rest.popleft()
            if i < num: i = num
            while check[i]:
                i += 1
            result += i - num
            check[i] = 1
            i += 1
        return result
            
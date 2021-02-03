class Solution:
    def trailingZeroes(self, n: int) -> int:
        from math import log
        if n == 0:
            return 0
        arr = []
        answer = 0
        for i in range(1,int(log(n)/log(5)+1)):
            arr.append(5**i)
        for j in range(len(arr)):
            answer += n//arr[j]
        return answer
class Solution:
    def isPowerOfTwo(self, n):
        list =[]
        for i in range(31):
            list.append(2**i)
        if n in list:
            return True
        return False
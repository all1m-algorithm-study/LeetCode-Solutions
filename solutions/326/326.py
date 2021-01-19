class Solution:
    def isPowerOfThree(self, n):
        import math
        list = []
        max_of_pow3 = int(31*math.log(2)/math.log(3))+1
        for i in range(max_of_pow3):
            list.append(3**i)
        if n in list:
            return True
        return False
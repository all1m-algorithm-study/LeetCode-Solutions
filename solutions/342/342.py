class Solution:
    def isPowerOfFour(self, n):
        list =[1]
        for i in range(1,16):
            list.append(4**i)
        if n in list:
            return True
        return False
class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1
        rev = int(str(abs(x))[::-1])*sign
        if abs(rev-0.5)>(2**31 - 0.5):
            return 0
        return rev
class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        elif x == 0 or abs(x-0.5)>(2**31 - 0.5:
            return 0
        else:
            sign = 1
        rev = int(str(abs(x))[::-1])*sign
        return rev

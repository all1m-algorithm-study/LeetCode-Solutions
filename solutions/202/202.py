class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        def calc(num):
            sum = 0
            len_num = int(math.log10(num)+1)
            for i in range(len_num):
                sum += int(str(num)[i])**2
            return sum
        ans = calc(n)
        while True:
            ans = calc(ans)
            if ans > 0 and ans < 10:
                break
        if ans == 1 or ans == 7:
            return True
        else:
            return False
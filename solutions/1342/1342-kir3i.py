class Solution:
    def numberOfSteps(self, num):
        if num == 0:
            return 0
        elif num % 2 == 0:
            return self.numberOfSteps(num//2) + 1
        else:
            return self.numberOfSteps(num-1) + 1

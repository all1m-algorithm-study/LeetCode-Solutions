class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        num, remainder = n // 3, n % 3
        if not remainder: return self.isPowerOfThree(num)
        else: return True if not num and remainder == 1 else False
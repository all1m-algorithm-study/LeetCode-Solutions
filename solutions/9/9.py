class Solution(object):
    def isPalindrome(self, x):
        from collections import deque
        word = deque(str(x))
        while len(word) > 1:
            if word.popleft() != word.pop():
                return False
        return True
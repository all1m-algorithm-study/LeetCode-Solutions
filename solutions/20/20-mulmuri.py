class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []

        for i in s:
            if i in left:
                stack.append(left.index(i))
            else:
                if len(stack) == 0:
                    return False
                if right.index(i) == stack[-1]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
        

class Solution:    
    def compress(self, chars):
        s, result = 0, [chars[0]]
        num = 1
        for i in range(1, len(chars)):
            if chars[s] == chars[i]: num += 1
            else:
                if num > 1: result += list(str(num))
                result.append(chars[i])
                s = i
                num = 1
        if num > 1: result += list(str(num))
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)
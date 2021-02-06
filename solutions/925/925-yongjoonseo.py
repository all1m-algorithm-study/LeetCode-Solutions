class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]: return False
        idx = 1
        for i in range(1, len(typed)):
            if idx < len(name) and typed[i] == name[idx]:
                idx += 1
                continue
            if typed[i] == typed[i-1]: continue
            else: return False
        if idx >= len(name): return True
        else: return False
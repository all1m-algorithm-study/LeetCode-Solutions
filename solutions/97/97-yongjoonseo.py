from collections import deque

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        if not s1 or not s2:
            string = s2 if not s1 else s1
            if s3 == string: return True
            else: return False
        q = deque([(0, 0)])
        visited = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
        i = 0
        while q:
            for _ in range(len(q)):
                a, b = q.popleft()
                if a < len(s1) and not visited[a+1][b] and s1[a] == s3[i]:
                    visited[a+1][b] = 1
                    q.append((a+1, b))
                if b < len(s2) and not visited[a][b+1] and s2[b] == s3[i]:
                    visited[a][b+1] = 1
                    q.append((a, b+1))
            i += 1
        return True if i == len(s3)+1 else False
                
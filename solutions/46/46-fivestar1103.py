class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def DFS(n):
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    tmp.append(nums[i])
                    ret.append(tmp.copy()) if n == len(nums) else DFS(n + 1)
                    visited[i] = False
                    tmp.pop()

        visited, tmp, ret = [False] * len(nums), [], []
        DFS(1)
        return ret
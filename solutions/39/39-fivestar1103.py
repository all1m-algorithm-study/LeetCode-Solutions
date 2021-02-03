class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(idx, target, tmp):
            if target == 0:
                ret.append(tmp)
            elif target > 0:
                for i in range(idx, len(candidates)):
                    DFS(i, target - candidates[i], tmp + [candidates[i]])

        ret = []
        DFS(0, target, [])
        return ret
class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        res, colCheck, diag1Check, diag2Check = [0], [False] * (n + 1), [False] * (2 * n), [False] * (2 * n)

        def solve(row):
            for i in range(1, n + 1):
                if not colCheck[i] and not diag1Check[row + i - 1] and not diag2Check[row - i + n]:
                    if row == n:
                        res[0] += 1
                    else:
                        colCheck[i], diag1Check[row + i - 1], diag2Check[row - i + n] = True, True, True
                        solve(row + 1)
                        colCheck[i], diag1Check[row + i - 1], diag2Check[row - i + n] = False, False, False

        solve(1)
        return res[0]
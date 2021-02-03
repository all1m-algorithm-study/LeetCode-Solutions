class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colCheck, tmp, res = [False] * (n + 1), [0], []
        diag1Check, diag2Check = [False] * (2 * n), [False] * (2 * n)

        def solve(row):
            for i in range(1, n + 1):
                if not colCheck[i] and not diag1Check[row + i - 1] and not diag2Check[row - i + n]:
                    tmp.append(i)
                    if row == n:
                        sol = []
                        for j in range(1, n + 1):
                            board = ["."] * n
                            board[tmp[j] - 1] = "Q"
                            sol.append("".join(board))
                        res.append(sol)
                    else:
                        colCheck[i], diag1Check[row + i - 1], diag2Check[row - i + n] = True, True, True
                        solve(row + 1)
                        colCheck[i], diag1Check[row + i - 1], diag2Check[row - i + n] = False, False, False
                    tmp.pop()

        solve(1)
        return res
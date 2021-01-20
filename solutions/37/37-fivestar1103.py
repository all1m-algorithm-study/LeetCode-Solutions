class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # empty: list of empty cells
        empty, whichBox = [], [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        rowCheck = [[False] * 10 for _ in range(9)]
        colCheck = [[False] * 10 for _ in range(9)]
        boxCheck = [[False] * 10 for _ in range(9)]
        # brute-force searching
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    # append empty cells as [row, column, box]
                    empty.append([i, j, whichBox[i // 3][j // 3]])
                else:
                    rowCheck[i][int(board[i][j])] = True
                    colCheck[j][int(board[i][j])] = True
                    boxCheck[whichBox[i // 3][j // 3]][int(board[i][j])] = True

        # backtracking
        flag = [False]
        def solve(idx):
            if flag[0]:
                # exit if flag is True
                import sys
                sys.exit()
            row, col, box = empty[idx][0], empty[idx][1], empty[idx][2]
            for i in range(1, 10):
                if not rowCheck[row][i] and not colCheck[col][i] and not boxCheck[box][i] and not flag[0]:
                    board[row][col] = str(i)
                    if idx + 1 == len(empty):
                        flag[0] = True
                        return board
                    rowCheck[row][i], colCheck[col][i], boxCheck[box][i] = True, True, True
                    solve(idx + 1)
                    rowCheck[row][i], colCheck[col][i], boxCheck[box][i] = False, False, False

        solve(0)

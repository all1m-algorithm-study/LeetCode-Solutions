import java.util.ArrayList;

class Solution {
	boolean[][] exist_row;
	boolean[][] exist_col;
	boolean[][] exist_sqr;
	char[][] board;
	ArrayList<int[]> blanks;

	public boolean dfs(int depth) {
		if (depth < 0) {
			return true;
		}
		int[] ij = blanks.get(depth);
		int i = ij[0], j = ij[1], sqr;
		sqr = i / 3 * 3 + j / 3;
		for (int n = 1; n <= 9; n++) {
			if (!(exist_row[i][n] || exist_col[j][n] || exist_sqr[sqr][n])) {
				exist_row[i][n] = exist_col[j][n] = exist_sqr[sqr][n] = true;
				board[i][j] = (char) n;
				if (dfs(depth - 1))
					return true;
				exist_row[i][n] = exist_col[j][n] = exist_sqr[sqr][n] = false;
				board[i][j] = 0;

			}
		}
		return false;
	}

	public void solveSudoku(char[][] board) {
		exist_row = new boolean[9][10];
		exist_col = new boolean[9][10];
		exist_sqr = new boolean[9][10];
		this.board = board;
		blanks = new ArrayList<>();

		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] == '.') {
					board[i][j] = 0;
					blanks.add(new int[] { i, j });
				} else
					board[i][j] -= '0';
				char n = board[i][j];
				exist_row[i][n] = true;
				exist_col[j][n] = true;
				exist_sqr[i / 3 * 3 + j / 3][n] = true;
			}
		}

		dfs(blanks.size() - 1);
		for (int i = 0; i < 9; i++)
			for (int j = 0; j < 9; j++)
				board[i][j] += '0';

	}
}
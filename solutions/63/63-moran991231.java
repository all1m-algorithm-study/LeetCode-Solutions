class Solution {
	public int uniquePathsWithObstacles(int[][] obstacleGrid) {
		int[][] og = obstacleGrid;
		int r = obstacleGrid.length, c = obstacleGrid[0].length;

		if (og[0][0] == 1)
			return 0;

		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (og[i][j] == 1) {
					og[i][j] = -1;
				}
			}

		og[0][0] = 1;
		for (int i = 1; i < r; i++)
			og[i][0] = Math.max(og[i][0] + og[i - 1][0], 0);

		for (int j = 1; j < c; j++)
			og[0][j] = Math.max(og[0][j] + og[0][j - 1], 0);

		for (int i = 1; i < r; i++) {
			for (int j = 1; j < c; j++) {
				if (og[i][j] != -1)
					og[i][j] = og[i - 1][j] + og[i][j - 1];
				else
					og[i][j] = 0;
			}
		}

		return og[r - 1][c - 1];
	}
}
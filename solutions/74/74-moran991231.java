class Solution {
	public static boolean searchMatrix(int[][] matrix, int target) {
		int r = matrix.length, c = matrix[0].length;

		int s = 0, e = r - 1, pr = 0, pc;
		while (s <= e) {
			pr = (s + e) / 2;
			if (matrix[pr][0] == target) return true;
			else if (matrix[pr][0] < target) s = pr + 1;
			else e = pr - 1;

		}

		if (pr == 0 && target < matrix[pr][0]) return false;
		else if (pr == 0 || pr == r - 1 && matrix[pr][0] < target);
		else {
			if (matrix[pr - 1][0] < target && target < matrix[pr][0]) pr--;
		}

		s = 0;
		e = c - 1;
		while (s <= e) {
			pc = (s + e) / 2;
			if (matrix[pr][pc] == target) return true;
			else if (matrix[pr][pc] < target) s = pc + 1;
			else e = pc - 1;
		}
		return false;
	}
}

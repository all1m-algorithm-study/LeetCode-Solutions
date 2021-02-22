class Solution {
	static int[][] C = new int[200][];  //dp

	static int get_nCk(int n, int k) {
		if (C[n] == null) {
			C[n] = new int[n + 1];
		}
		if (k == 0 || k == n) {
			C[n][0] = C[n][k] = 1;
			return 1;
		}
		if (C[n][k] == 0) {
			C[n][k] = get_nCk(n - 1, k - 1) + get_nCk(n - 1, k);
		}
		return C[n][k];

	}

	public int uniquePaths(int m, int n) {
		int N = m + n - 2;
		int K = Math.min(m, n) - 1;
		return get_nCk(N, K);
	}
}
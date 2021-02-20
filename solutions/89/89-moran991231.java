class Solution {
	public List<Integer> grayCode(int n) {
		int gray = 0, pow2_n = (int) Math.pow(2, n);
		List<Integer> ret = new ArrayList<Integer>(pow2_n);
		ret.add(gray);
		for (int i = 1; i < pow2_n; i++) {
			for (int k = 0; k < n; k++) {
				if ((i & (1 << k)) != 0) {
					gray = gray ^ (i & 1 << k);
					ret.add(gray);
					break;
				}
			}
		}

		return ret;

	}
}
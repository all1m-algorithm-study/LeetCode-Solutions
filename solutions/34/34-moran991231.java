class Solution {

	public static int[] searchRange(int[] nums, int target) {
		int s = 0, e = nums.length - 1, idx;
		int[] ret = { -1, -1 };
		if (e < 0)
			return ret;
		if (e == 0) {
			ret = (nums[0] == target) ? new int[2] : ret;
			return ret;
		}

		while (s <= e) {
			idx = (s + e) / 2;
			if (nums[idx] <= target) {
				if (s == idx) {
					if (nums[idx + 1] == target)
						ret[1] = idx + 1;
					else if (nums[idx] == target)
						ret[1] = idx;
					else
						return ret;
					break;
				}
				s = idx;
			} else {
				e = idx - 1;
			}
		}
		if (e < s)
			return ret;

		s = 0;
		e = nums.length - 1;
		while (s <= e) {
			idx = (s + e+1) / 2;
			if (target <= nums[idx]) {
				if (e == idx) {
					if (nums[idx - 1] == target)
						ret[0] = idx - 1;
					else if (nums[idx] == target)
						ret[0] = idx;
					break;
				}
				e = idx;
			} else {
				s = idx + 1;
			}
		}

		return ret;
	}
}
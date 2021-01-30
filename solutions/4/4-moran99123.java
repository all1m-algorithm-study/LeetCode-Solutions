// 정답 제출은 됐는데 왜 정답인지 모르겠음
class Solution {

	public int search(int[] arr, int s1, int e1, int val) {
		int idx = (s1 + e1) / 2;
		if (arr[e1] <= val)
			return e1 + 1;
		if (val < arr[s1])
			return s1 - 1;
		while (s1 <= e1) {
			if (arr[idx] <= val && val <= arr[idx + 1])
				break;
			idx = (s1 + e1) / 2;
			if (val < arr[idx]) {
				e1 = idx - 1;
			} else if (arr[idx] < val) {
				s1 = idx + 1;
			} else
				s1 = idx + 1;
		}
		return idx;
	}

	double if_length_1(int num, int[] nums, int s, int e, int ti) {
		int idx = search(nums, s, e, num);
		if (ti + s <= idx) {
			if (ti + s > e)
				return num;
			return nums[ti + s];
		} else if (ti + s == idx + 1)
			return num;
		else
			return nums[ti + s - 1];

	}

	public double func(int[] nums1, int[] nums2, int s1, int e1, int s2, int e2, int ti) {

		if (s1 > e1)
			return nums2[s1 + ti];
		if (s2 > e2)
			return nums1[s1 + ti];

		if (s1 == e1) {
			return if_length_1(nums1[s1], nums2, s2, e2, ti);

		} else if (s2 == e2) {
			return if_length_1(nums2[s2], nums1, s1, e1, ti);

		}

		double ratio = ((double) ti) / (e1 + e2 - s1 - s2 + 2);
		int p1 = (int) (s1 + ratio * (e1 - s1 + 1));
		int p2 = (int) (s2 + ratio * (e2 - s2 + 1));

		if (nums1[p1] == nums2[p2])
			return nums1[p1];
		else if (nums1[p1] < nums2[p2]) {
			return func(nums1, nums2, p1, e1, s2, p2, ti - (p1 - s1));
		} else {
			return func(nums1, nums2, s1, p1, p2, e2, ti - (p2 - s2));
		}

	}

	public double findMedianSortedArrays(int[] nums1, int[] nums2) {
		int a = nums1.length, b = nums2.length;

		if ((a + b) % 2 == 1) {
			double ret = func(nums1, nums2, 0, a - 1, 0, b - 1, (a + b) / 2);
			return ret;
		} else {
			double ret1, ret2;
			ret1 = func(nums1, nums2, 0, a - 1, 0, b - 1, (a + b - 1) / 2);
			ret2 = func(nums1, nums2, 0, a - 1, 0, b - 1, (a + b - 1) / 2 + 1);
			return (ret1 + ret2) / 2.0;
		}

	}
}

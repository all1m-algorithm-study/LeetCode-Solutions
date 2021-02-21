/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
	let sum = m + n - 1;
	m--;
	n--;
	while (n >= 0) {
		if (nums1[m] > nums2[n]) {
			nums1[sum--] = nums1[m--];
		} else {
			nums1[sum--] = nums2[n--];
		}
	}

	return nums1;
};

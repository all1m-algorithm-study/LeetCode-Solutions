/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
	const comp = (a, b) => a - b;
	nums.sort(comp);
	return nums;
};

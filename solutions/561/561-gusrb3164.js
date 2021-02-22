/**
 * @param {number[]} nums
 * @return {number}
 */
const comp = (a, b) => a - b;
var arrayPairSum = function (nums) {
	nums.sort(comp);
	let sum = 0;
	for (var i = 0; i < nums.length; i += 2) {
		sum += nums[i];
	}
	return sum;
};

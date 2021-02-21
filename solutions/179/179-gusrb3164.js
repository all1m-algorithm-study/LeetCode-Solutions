/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function (nums) {
	const comp = (a, b) => {
		return Number(String(b) + String(a)) - Number(String(a) + String(b));
	};
	nums.sort(comp);
	var result = '';
	for (var i in nums) {
		result += String(nums[i]);
	}
	if (Number(result) === 0) {
		return '0';
	}
	return result;
};

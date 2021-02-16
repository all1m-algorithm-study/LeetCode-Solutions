/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	let dict = {};
	for (let i = 0; i < nums.length; i++) {
		dict[nums[i]] = i;
	}
	for (let i = 0; i < nums.length - 1; i++) {
		const tmp = target - nums[i];
		if (dict[tmp] !== undefined && dict[tmp] !== i) {
			return [i, dict[tmp]];
		}
	}
};

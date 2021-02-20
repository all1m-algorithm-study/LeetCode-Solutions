/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
	let red = 0;
	let white = 0;
	let blue = nums.length;
	while (white < blue) {
		//red 일 때
		if (nums[white] < 1) {
			const tmp = nums[white];
			nums[white] = nums[red];
			nums[red] = tmp;
			red++;
			white++;
		} // blue 일 때
		else if (nums[white] > 1) {
			blue--;
			const tmp = nums[white];
			nums[white] = nums[blue];
			nums[blue] = tmp;
		} // white 일 때
		else {
			white++;
		}
	}
};

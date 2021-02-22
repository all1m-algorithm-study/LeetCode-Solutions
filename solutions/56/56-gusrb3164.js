/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
	const comp = (a, b) => {
		if (a[0] === b[0]) return a[1] - b[1];
		return a[0] - b[0];
	};
	let merge = [];
	intervals.sort(comp);
	for (let i = 0; i < intervals.length; i++) {
		let end = merge.length - 1;
		if (end > -1 && merge[end][1] >= intervals[i][0]) {
			merge[end][1] = Math.max(merge[end][1], intervals[i][1]);
		} else {
			merge.push(intervals[i]);
		}
	}
	return merge;
};

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
	var s = s.split('').sort().join('');
	var t = t.split('').sort().join('');
	if (s === t) return true;
	return false;
};

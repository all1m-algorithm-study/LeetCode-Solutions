class Solution {
	 int longest_len = 0;
	 int longest_s, longest_e;

	public  void calc(String str, int start, int end) {
		int s, e;
		for (s = start, e = end; s <= e; s++, e--)
			if (str.charAt(s) != str.charAt(e))
				return;
		if (longest_len < (end - start + 1)) {
			longest_len = (end - start + 1);
			longest_s = start;
			longest_e = end;
		}
	}

	public  String longestPalindrome(String s) {
		int len = s.length();
		for (int start = 0; start < len; start++) {
			for (int end = start+longest_len; end < len; end++) {
				calc(s, start, end);
			}
		}
		System.out.println(longest_len);
		return s.substring(longest_s, longest_e+1);
	}
}
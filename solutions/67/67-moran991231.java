class Solution {
	public String addBinary(String a, String b) {
		int len_a = a.length(), len_b = b.length();
		char[] ret = new char[Math.max(len_a, len_b) + 1];

		// swap
		if (len_b > len_a) {
			String temp = a;
			a = b;
			b = temp;
			int temp_ = len_a;
			len_a = len_b;
			len_b = temp_;
		}

		int pa = len_a - 1, pb = len_b - 1, pr = ret.length - 1;
		char ch_a, ch_b, carry = '0';
		int sum;

		for (; 0 <= pb; pa--, pb--, pr--) {
			ch_a = a.charAt(pa);
			ch_b = b.charAt(pb);
			sum = ch_a + ch_b + carry - 2 * '0';
			if (sum >= '2') {
				ret[pr] = (char) (sum - 2);
				carry = '1';
			} else {
				ret[pr] = (char) sum;
				carry = '0';
			}
		}

		for (; 0 <= pa; pa--, pr--) {
			ch_a = a.charAt(pa);
			sum = ch_a + carry - '0';
			if (sum >= '2') {
				ret[pr] = (char) (sum - 2);
				carry = '1';
			} else {
				ret[pr] = (char) sum;
				carry = '0';
			}
		}
		ret[0] = carry;

		if (ret[0] == '0') {
			return new String(ret, 1, len_a);
		}else {
			return new String(ret);
		}
	}
}
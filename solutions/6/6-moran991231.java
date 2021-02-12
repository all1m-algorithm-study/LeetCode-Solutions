class Solution {
	static StringBuilder sb;

	static public String convert(String s, int numRows) {
		int len = s.length();
		int cursor, jump;
		if (numRows == 1)
			return s;
		sb = new StringBuilder(numRows * (len / 2 + 1));
		for (int r = 0; r < numRows; r++) {
			cursor = -1;
			jump = r + 1;
			while (cursor < len) {
				if (jump != 0) {
					cursor += jump;
					if (!(cursor < len))
						break;
					sb.append(s.charAt(cursor));
				}

				jump = (numRows - 1 - r) * 2;
				if (jump != 0) {
					cursor += jump;
					if (!(cursor < len))
						break;
					sb.append(s.charAt(cursor));
				}
				
				jump = r * 2;
			}
		}
		return sb.toString();
	}

}
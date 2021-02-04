#define ORD(C) C-97

class Solution {
public:
	int le[26];
	int re[26];
	vector<int> ans;
	vector<int> partitionLabels(string S) {
		memset(le, -1, sizeof(le));
		memset(re, -1, sizeof(re));
		int sz = S.size();

		// First Scan
		for (int i = 0; i < sz; i++) {
			if (le[ORD(S[i])] == -1)
				le[ORD(S[i])] = i;
			re[ORD(S[i])] = i;
		}

		// Second Scan
		int cnt = 0, sp = 0;
		for (int i = 0; i < sz; i++) {
			if (!cnt)	sp = i;
			if (le[ORD(S[i])] == i)	cnt += 1;
			if (cnt == 1 && re[ORD(S[i])] == i)
				ans.push_back(i - sp + 1);
			if (re[ORD(S[i])] == i)	cnt -= 1;
		}

		return ans;
	}
};
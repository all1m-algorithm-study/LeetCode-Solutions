#include <queue>
#include <set>
#include <string.h>
using namespace std;

class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		int answer = 0;
		queue<char> q;
        set<char> st;
		int count = 0;

		if (s[0] == ' ' || s.size() == 1)
			return 1;
        q.push(s[0]);
        st.insert(s[0]);
        for (int i=1;i<s.size();i++){
            if (st.find(s[i]) == st.end()){ //Áßº¹x
                q.push(s[i]);
                st.insert(s[i]);
            }
            else {
                while (q.front() != s[i]){
                    st.erase(st.find(q.front()));
                    q.pop();
                }
                q.pop();
                q.push(s[i]);
            }
            if (q.size() > answer)
                answer = q.size();
        }
		return answer;
	}
};

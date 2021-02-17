class Solution {
public:
    int cnt[26];
    int ans;
    int minSteps(string s, string t) {
        for(const char &c: s)
            cnt[c-'a']++;
        for(const char &c: t)
            if(cnt[c-'a']-- <= 0)
                ans++;
        return ans;
    }
};

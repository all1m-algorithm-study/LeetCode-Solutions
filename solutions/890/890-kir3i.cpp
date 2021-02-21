class Solution {
public:
    
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        int sz = pattern.size();
        vector<string> ans;
        for(const string &w: words) {
            bool ok = true;
            unordered_map<char, char> trans;
            unordered_set<char> used;
            for(int i=0; i<sz && ok; i++) {
                if(trans.find(pattern[i]) == trans.end()) {
                    ok &= (used.find(w[i]) == used.end());
                    trans[pattern[i]] = w[i];
                    used.insert(w[i]);
                }
                else {
                    ok &= (trans[pattern[i]] == w[i]);
                }
            }
            if(ok)
                ans.push_back(w);
        }
        return ans;
    }
};

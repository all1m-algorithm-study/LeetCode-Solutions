class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        int sz = s.size();
        char* ans = new char[sz+1];
        ans[sz] = '\0';
        for(int i=0; i<sz; i++)
            ans[indices[i]] = s[i];
        return ans;
    }
};

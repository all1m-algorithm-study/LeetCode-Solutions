class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> ans = {first};
        for(const int &x: encoded)
            ans.push_back(ans.back()^x);
        return ans;
    }
};

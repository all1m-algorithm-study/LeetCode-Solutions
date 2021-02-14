class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        unordered_map<int, int> cnt;
        vector<int> t = nums;
        sort(t.begin(), t.end());
        for(int i=0; i<t.size(); i++)
            if(!cnt.count(t[i]))
                cnt[t[i]] = i;
        
        vector<int> ans;
        for(const int &x: nums)
            ans.push_back(cnt[x]);
        return ans;
    }
};

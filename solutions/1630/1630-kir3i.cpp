class Solution {
public:
    unordered_set<int> s;
    int smax, smin;
    vector<bool> ans;
    bool ok;
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        int qsz = l.size();
        for (int q=0; q<qsz; q++) {
            s.clear();
            smax = -2e8;
            smin = 2e8;
            ok = true;
            for(int i=l[q]; i<=r[q]; i++) {
                s.insert(nums[i]);
                smax = max(smax, nums[i]);
                smin = min(smin, nums[i]);
            }
            
            int jump = (smax - smin) / (r[q] - l[q]);
            if (smin == smax) {
                ans.push_back(true);
                continue;
            } else if(!jump) {
                ans.push_back(false);
                continue;
            }
            for(int i=smin; i<=smax; i+=jump) {
                if(!s.count(i)) {
                    ans.push_back(false);
                    ok = false;
                    break;
                }
            }
            
            if (ok)
                ans.push_back(true);
        }
        return ans;
    }
};
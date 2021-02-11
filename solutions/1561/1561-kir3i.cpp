class Solution {
public:
    int ans = 0;
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());
        int sz = piles.size();
        for(int i=sz/3; i<sz; i+=2)
            ans += piles[i];
        return ans;
    }
};

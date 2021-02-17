class Solution {
public:
    int countVowelStrings(int n) {
        return nHr(5, n);
    }
    
    int nHr(int n, int r) {
        double ans = 1.;
        for(int i=0; i<r; i++)
            ans *= 1.0 * (n+r-1-i) / (i+1);
        return round(ans);
    }
};
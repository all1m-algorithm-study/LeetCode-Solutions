class Solution {
    public int[] cnt = new int[26];
    public int ans = 0;
    public int minSteps(String s, String t) {
        for(int i=0; i<s.length(); i++)
            cnt[s.charAt(i)-'a']++;
        for(int i=0; i<t.length(); i++)
            if(cnt[t.charAt(i)-'a']-- <= 0)
                ans++;
        return ans;
    }
}

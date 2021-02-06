class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max=0;
        int []exist = new int[128]; 
        int pl=0,pr=0;
        int s_len=s.length();
        int len;
        char ch;
        while(pr<s_len) {
        	ch= s.charAt(pr);
        	if(exist[ch]<=pl) { // ch dosesn't exist in sub_s
        		exist[ch]=++pr;
        	}else { // ch exists in sub_s
        		len = pr-pl;
        		max = (max>len)?max:len;
        		pl=exist[ch];
        		exist[ch]=++pr;
        	}
        }
        len = pr-pl; //calculate sub_s length which is located at the end of s
        max=(max>len)?max:len;
        return max;    	
    }
}
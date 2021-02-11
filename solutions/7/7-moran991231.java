class Solution {
    public int reverse(int x) {
        if (x==0) return 0;
        int sign = (x>0)? 1:-1;
        long ret=0;
        x *= sign;
        while (x%10 == 0) x/=10;
        
        while (x !=0) {
        	ret *=10;
        	ret += x%10;
        	x/=10;        	
        }
        ret *= sign;
        if (ret <Integer.MIN_VALUE || Integer.MAX_VALUE<ret) return 0;
        return (int) ret;
    }
}
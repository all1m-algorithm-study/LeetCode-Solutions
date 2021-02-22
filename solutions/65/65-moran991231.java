class Solution {
	
	static boolean isDigit(char ch) {
		if('0'<= ch && ch <= '9') return true;
		return false;
	}
	
	static boolean isSign(char ch) {
		if(ch == '+'|| ch=='-') return true;
		return false;
	}
	
	static boolean isDecimal(String s) {
		int dot = s.indexOf('.');
		int len = s.length();
		if(!(0<=dot && dot < len)) return false;
		int s_i = (isSign(s.charAt(0)))? 1: 0;
		
		if(s_i==dot && dot ==len-1 ) return false;
		
		if(dot != len-1) {
			for(int i=dot+1; i<len; i++)
				if(!isDigit(s.charAt(i))) return false;
		}
		if(s_i != dot) {
			for(int i=s_i; i<dot; i++)
				if(!isDigit(s.charAt(i))) return false;
		}
		return true;
	}
	
	static boolean isInteger(String s) {
		char ch = s.charAt(0);
		
		if(s.length()==1) 
			return isDigit(ch);
		
		if(isDigit(ch)||isSign(ch)) {
			for(int i=1; i<s.length(); i++) {
				if(!isDigit(s.charAt(i))) return false;
			}
		}else return false;
		
		return true;
	}
	
    public boolean isNumber(String s) {  // main
    	int len = s.length();
    	char ch;
    	
    	ch= s.charAt(0);    	
    	if(ch == 'e'|| ch=='E') return false;
    	ch = s.charAt(len-1);
    	if(ch=='e'||ch=='E') return false;
    	
    	String[] comp = s.split("e|E");
    	
    	if(comp.length>2) return false;
    	if(comp.length ==1) {
    		if(!(isDecimal(comp[0])||isInteger(comp[0]))) return false;
    	}else {
    		if(!(isDecimal(comp[0])||isInteger(comp[0]))) return false;
    		if(!isInteger(comp[1])) return false;
    	}
    	
    	return true;
    }
}
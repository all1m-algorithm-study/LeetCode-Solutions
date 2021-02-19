class Solution {
    public int openCnt = 0;
    public int closeCnt = 0;
    public int minAddToMakeValid(String S) {
        for(int i=0; i<S.length(); i++) {
            if (S.charAt(i) == '(')
                openCnt++;
            else if(S.charAt(i) == ')') {
                if (openCnt > 0)
                    openCnt--;
                else
                    closeCnt++;
            }
        }
        return openCnt + closeCnt;
    }
}

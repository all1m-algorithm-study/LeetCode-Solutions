class Solution {
public:
    stack<char> s;
    int minAddToMakeValid(string S) {
        for(const char &c: S) {
            if(c=='(')
                s.push(c);
            else if(c==')') {
                if(!s.empty() && s.top() == '(')
                    s.pop();
                else
                    s.push(')');
            }
        }
        return s.size();
    }
};

#include <vector>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        vector<string> zigzag(numRows,"");
        int row = 0;
        bool direction = 0; // 0:down(++), 1:up(--)
        
        if (numRows == 1)
            return s;
        for (int i=0;i<s.size();i++){
            zigzag[row].push_back(s[i]);
            if (direction==0)
                row++;
            else
                row--;
            if (row == numRows){
                row-=2;
                direction = !direction;
            }
            if (row == -1){
                row+=2;
                direction = !direction;
            }
        }
        string result="";
        for (int i=0;i<numRows;i++){
            result += zigzag[i];
        }
        return result;
    }
};

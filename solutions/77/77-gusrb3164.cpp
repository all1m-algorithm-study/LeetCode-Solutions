class Solution
{
public:
    vector<vector<int>> result;
    int gN;

    vector<vector<int>> combine(int n, int k)
    {
        vector<int> output;
        gN = n;

        for (int i = 1; i <= gN - k + 1; i++)
        {
            vector<int> tmp;
            tmp.push_back(i);
            recur(i + 1, k - 1, tmp);
        }
        return result;
    }
    void recur(int start, int rem, vector<int> output)
    {
        if (rem == 0)
        { //남은 개수가 0이되면 끝
            result.push_back(output);
            return;
        }
        for (int i = start; i <= gN - rem + 1; i++)
        {
            vector<int> tmp = output; //덮어 씌여지지 않게 우선 복사
            tmp.push_back(i);
            recur(i + 1, rem - 1, tmp);
        }
    }
};
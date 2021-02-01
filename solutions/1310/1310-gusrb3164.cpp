class Solution
{
public:
    vector<int> xorQueries(vector<int> &arr, vector<vector<int>> &queries)
    {
        vector<int> result;
        vector<int> xorBoard;

        xorBoard.push_back(arr[0]);
        //0~ i 까지 xor 한것을 차례대로 저장
        for (int i = 1; i < arr.size(); i++)
        {
            xorBoard.push_back(xorBoard[i - 1] ^ arr[i]);
        }

        // 해당 끝 인덱스까지의 xor 한 것과 해당 시작 인덱스 전 까지의 xor 한 걸 xor 하면 시작과 끝 사이의 xor 이 나옴.
        for (auto query : queries)
        {
            int tmp;
            if (query[0] == 0)
            {
                tmp = xorBoard[query[1]];
            }
            else
            {
                tmp = xorBoard[query[1]] ^ xorBoard[query[0] - 1];
            }
            result.push_back(tmp);
        }
        return result;
    }
};
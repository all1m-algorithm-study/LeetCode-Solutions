class Solution
{
public:
    vector<vector<int>> result;
    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<int> left;
        recur(left, nums);
        return result;
    }
    void recur(vector<int> left, vector<int> nums)
    {
        if (nums.empty())
            result.push_back(left);

        for (int i = 0; i < nums.size(); i++)
        {
            //이전 값을 반복 사용하므로 덮어쓰지 않게 우선 복사
            vector<int> tmpLeft = left;
            vector<int> tmpNums = nums;

            tmpLeft.push_back(tmpNums[i]);
            tmpNums.erase(tmpNums.begin() + i);
            recur(tmpLeft, tmpNums);
        }
    }
};
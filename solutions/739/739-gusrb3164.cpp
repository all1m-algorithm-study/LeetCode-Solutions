class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &T)
    {
        vector<int> stack;               //T의 값에 접근할 인덱스를 스택으로 저장
        vector<int> result(T.size(), 0); // 각 T에 대응하는 날짜 저장

        for (int i = 0; i < T.size(); i++)
        {
            while (!stack.empty() && T[stack.back()] < T[i])
            {
                result[stack.back()] = i - stack.back();
                stack.pop_back();
            }
            stack.push_back(i);
        }
        return result;
    }
};
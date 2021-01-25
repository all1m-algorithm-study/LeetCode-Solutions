class Solution
{
public:
    int numJewelsInStones(string jewels, string stones)
    {
        set<char> mJewel;
        int result = 0;
        // 보석들을 키 리스트에 저장
        for (auto i : jewels)
        {
            mJewel.insert(i);
        }
        //키 리스트에 보석이 있다면 결과 +1
        for (auto i : stones)
        {
            if (mJewel.find(i) != mJewel.end())
            {
                result++;
            }
        }
        return result;
    }
};
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int result = 0;

        for (int i = 0; i < s.size(); i++)
        {
            int len = 0;
            unordered_map<char, int> uMap;

            while (i < s.size())
            {
                if (uMap.find(s[i]) == uMap.end())
                {
                    uMap.insert(make_pair(s[i], i));
                    len++;
                    i++;
                }
                else
                {
                    i = uMap[s[i]]; //겹친다면 해당 겹치는 부분 다음부터 다시 시작해야하므로 해당 인덱스로 돌아감
                    break;
                }
            }
            result = max(result, len);
        }
        return result;
    }
};
class Solution
{
public:
    int romanToInt(string s)
    {
        int sum = 0;
        unordered_map<char, int> um = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};

        for (int i = 0; i < s.size(); i++)
        {
            if (i < s.size() - 1 && um[s[i]] < um[s[i + 1]])
            {
                sum -= um[s[i]];
            }
            else
            {
                sum += um[s[i]];
            }
        }
        return sum;
    }
};
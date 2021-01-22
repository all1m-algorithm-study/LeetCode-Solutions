class Solution
{
public:
    string removeDuplicateLetters(string s)
    {
        int cnt[26] = {}, isUse[26] = {};
        string result = "";

        for (auto i : s)
        {
            cnt[i - 'a']++;
        }
        for (auto i : s)
        {
            if (isUse[i - 'a'] > 0)
            {
                cnt[i - 'a']--;
                continue;
            }
            while (!result.empty() && result.back() > i && cnt[result.back() - 'a'] > 0)
            {
                isUse[result.back() - 'a']--;
                result.pop_back();
            }
            result.push_back(i);
            isUse[i - 'a']++;
            cnt[i - 'a']--;
        }
        return result;
    }
};
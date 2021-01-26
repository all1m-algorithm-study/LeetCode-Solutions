class Solution
{
public:
    string arr[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> result;
    vector<string> letterCombinations(string digits)
    {
        if (!digits.empty())
        {
            comb(digits, "");
        }
        return result;
    }

    void comb(string &digits, string prev)
    {
        if (prev.size() == digits.size())
        {
            result.push_back(prev);
            return;
        }
        for (auto i : arr[digits[prev.size()] - '0'])
        {
            string tmp = prev;
            tmp.push_back(i);
            comb(digits, tmp);
        }
    }
};
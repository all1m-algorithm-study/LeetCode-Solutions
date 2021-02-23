#include <string>
#include <algorithm>
class Solution
{
public:
	void reverseString(vector<char> &s)
	{
		vector<char> str;
		for (int i = s.size() - 1; i >= 0; i--)
		{
			char word = s[i];
			str.push_back(word);
		}
		s.erase(s.begin(), s.end());
		for (int i = 0; i < str.size(); i++)
		{
			char word = str[i];
			s.push_back(word);
		}
	}
};
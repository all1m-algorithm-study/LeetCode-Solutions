class Solution
{
public:
	bool isPalindrome(string s)
	{
		int left = 0, right = 0;

		for (int i = 0; i < strlen(s); i++)
		{
			// 영문자가 아니면 left 증가
			while (!isalnum(s[i + left]))
			{
				left++;
				if (i + left == strlen(s))
				{
					return true;
				}
			}
			while (!isalnum(s[strlen(s) - i - right]))
			{
				right++;
			}

			if (i + left >= strlen(s) - i - right)
				break;
			// 팰린드롬
			if (tolower(s[i + left]) != tolower(s[strlen(s) - i - right])) // tolower: 소문자로 변경, toupper: 대문자로 변경
			{
				return false;
			}
		}
		return true;
	}
};
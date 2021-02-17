class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0)
        {
            return false;
        }
        int tmp = x;
        long long int reverse = 0;
        while (tmp > 0)
        {
            reverse = reverse * 10 + (tmp % 10);
            tmp /= 10;
        }
        if (reverse == x)
            return true;
        return false;
    }
};
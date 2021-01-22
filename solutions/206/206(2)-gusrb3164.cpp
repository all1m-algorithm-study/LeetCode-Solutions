/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        return reverse(head);
    }
    ListNode *reverse(ListNode *node, ListNode *prev = nullptr)
    {
        if (node == nullptr)
        {
            return prev;
        }
        ListNode *next = node->next;
        node->next = prev;
        return reverse(next, node);
    }
};
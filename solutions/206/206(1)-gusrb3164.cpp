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
        ListNode *node = head;
        ListNode *prev = nullptr;
        while (node != nullptr)
        {
            ListNode *next = node->next;
            node->next = prev;
            prev = node;
            node = next;
        }
        return prev;
    }
};
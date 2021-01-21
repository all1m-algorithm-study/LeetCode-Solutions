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
    ListNode *reverseBetween(ListNode *head, int m, int n)
    {
        if (head == nullptr || m == n)
            return head;
        ListNode *start = new ListNode();
        ListNode *root = start;
        start->next = head;

        for (int i = 1; i < m; i++)
        {
            start = start->next;
        }
        ListNode *end = start->next; //end 는 reverse할 마지막 노드까지 이동하는 idx
        ListNode *tmp = end;         //tmp 는 reverse의 처음 부분 idx로 계속 갱신하는 역할
        ListNode *tmp2;              //tmp2 는 reverse 의 다음 부분 노드를 기억해서 reverse 마지막을 연결하는 역할
        for (int i = 0; i < n - m; i++)
        {
            tmp2 = end->next->next;
            end->next->next = tmp;
            tmp = end->next;
            end->next = tmp2;
            start->next = tmp;
        }
        return root->next;
    }
};
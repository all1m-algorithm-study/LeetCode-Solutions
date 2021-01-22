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
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        //우선순위 큐를 활용
        priority_queue<int, vector<int>, greater<int>> pq;

        //모든 값을 우선순위 큐에 저장
        for (auto list : lists)
        {
            while (list != nullptr)
            {
                pq.push(list->val);
                list = list->next;
            }
        }

        ListNode *head = new ListNode();
        ListNode *tail = head;

        while (!pq.empty())
        {
            ListNode *tmp = new ListNode(pq.top());
            pq.pop();
            tail->next = tmp;
            tail = tail->next;
        }
        return head->next;
    }
};
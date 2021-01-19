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
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* node=new ListNode(0);
        ListNode* head=node; //node 와 head가 처음에 동시에 참조하다가 node는 추가하면서 움직이고 최종 결과는 본래 그대로인 head반납
        int carry=0;
        
        while (l1!=nullptr||l2!=nullptr||carry>0){
            int sum=carry;
            if (l1!=nullptr){
                sum+=l1->val;
                l1=l1->next;
            }
            if(l2!=nullptr){
                sum+=l2->val;
                l2=l2->next;
            }
            
            carry=sum/10;
            node->next=new ListNode(sum%10);
            node=node->next;
        }
        return head->next;
    }
};
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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *p = list1, *idxS, *idxE;
        for(int i=0; i<a-1; i++)
            p = p->next;
        idxS = p;	// list1[a-1]
        
        for(int i=0; i<b-a+2; i++)
            p = p->next;
        idxE = p;	// list1[b+1]
        
        idxS->next = list2;
        
        while(list2->next)
            list2 = list2->next;
        list2->next = idxE;
        
        return list1;
    }
};

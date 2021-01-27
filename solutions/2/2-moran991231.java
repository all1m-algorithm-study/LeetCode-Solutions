/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head= new ListNode(0,new ListNode(0));
        ListNode cur =head;
        int sum;
        
        while(l1 !=null || l2 !=null){ // l1과 l2가 모두 null이 되기 전까지 반복
            cur=cur.next;
            sum = cur.val;
            if(l1 != null) {sum += l1.val; l1=l1.next;}
            if(l2 != null) {sum += l2.val; l2=l2.next;}
            cur.val=sum%10;
            cur.next = new ListNode(sum/10); //다음 노드에 carry를 전달
        }
        if(cur.next.val==0) cur.next=null; //마지막 노드의 값이 0이면 노드를 삭제한다.
        return head.next;
    }
}
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
	public ListNode rotateRight(ListNode head, int k) {
		int len = 1;
		ListNode tail = head;
		ListNode new_head, new_tail;
		int num;

		if (head == null || head.next == null)
			return head; // 0<= len <= 1

		// 2 <= len
		while (tail.next != null) {
			tail = tail.next;
			len++;
		}
		k %= len;
		if(k==0) return head;
		System.out.print(len);

		new_tail = head;
		for (int i = 0; i < len - k - 1; i++)
			new_tail = new_tail.next;
		new_head = new_tail.next;
		new_tail.next = null;
		tail.next = head;

		return new_head;

	}
}
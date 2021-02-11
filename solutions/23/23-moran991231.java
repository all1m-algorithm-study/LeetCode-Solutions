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
	
	public static ListNode endOf(ListNode node) {
		while (node.next != null) {
			node = node.next;
		}
		return node;
	}
	public static ListNode mergeKLists(ListNode[] lists) {
		int len = lists.length;
		ListNode head = null;
		ListNode[] nodes = new ListNode[20_001];
		ListNode temp;
		for (int i = 0; i < len; i++) {
			while (lists[i] != null) {
				temp = lists[i];
				lists[i] = temp.next; // pop head node in lists[i]
				temp.next = nodes[temp.val + 10000]; // push
				nodes[temp.val + 10000] = temp;
			}
		}

		// find head
		int start;
		for (start = 0; start < 20001; start++) {
			if (nodes[start] != null) {
				head = nodes[start];
				break;
			}
		}
		if (head != null) 
			temp = endOf(head);			
		 else temp = null;
		 //merge
		for(int i=start+1; i<20001; i++) {
			if (nodes[i]== null) continue;
			temp.next=nodes[i];
			temp = endOf(nodes[i]);
		}

		return head;

	}
}

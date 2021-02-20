/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var insertionSortList = function (head) {
	const root = new ListNode();
	while (head !== null) {
		let cur = root;
		while (cur.next && cur.next.val < head.val) {
			cur = cur.next;
		}
		const tmp = head.next;
		head.next = cur.next;
		cur.next = head;
		head = tmp;
	}
	return root.next;
};

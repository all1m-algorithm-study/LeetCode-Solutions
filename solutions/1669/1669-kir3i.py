# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        p = list1
        for _ in range(a-1):
            p = p.next
        idxS = p    # list1[a-1]

        for _ in range(b-a+2):
            p = p.next
        idxE = p    # list1[b+1]

        idxS.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = idxE

        return list1

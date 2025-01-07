# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode()
        dum.next = head
        cur = dum
        temp = dum

        for i in range(n):
            temp = temp.next

        while temp:
            prev = cur
            cur = cur.next
            temp = temp.next

        prev.next = cur.next
        return dum.next
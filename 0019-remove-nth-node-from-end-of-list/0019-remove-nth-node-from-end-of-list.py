# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(-1, head)
        cur = dum
        
        size = 0
        while cur.next:
            cur = cur.next
            size += 1

        travel = size - n
        cur = head
        prev = dum
        for i in range(travel):
            prev = cur
            cur = cur.next

        # adjust pointers
        prev.next = cur.next

        return dum.next


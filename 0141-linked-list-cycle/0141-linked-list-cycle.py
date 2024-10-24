# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        
        # dum = ListNode()
        slow = head
        fast = head.next.next

        while fast and slow:
            if slow == fast:
                return True
            # move the pointers
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
        return False
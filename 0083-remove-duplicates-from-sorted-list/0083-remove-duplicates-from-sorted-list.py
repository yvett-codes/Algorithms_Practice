# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = cur

        while cur:
            cur = cur.next
            
            if not cur:
                return head
            
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = prev.next
            
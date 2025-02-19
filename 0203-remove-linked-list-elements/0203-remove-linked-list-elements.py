# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = cur = dum  = ListNode(0, head)

        while cur.next:
            cur = prev.next
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
        return dum.next
        
        # Time: O(n)
        # Space: O(1)
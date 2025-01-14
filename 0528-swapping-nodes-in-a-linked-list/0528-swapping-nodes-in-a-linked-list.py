# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dum = ListNode(0, head)
        left = right = dum

        for i in range(k):
            left = left.next
        while left:
            left = left.next
            right = right.next

        left = dum
        for i in range(k):
            left = left.next

        temp = left.val
        left.val = right.val
        right.val = temp

        return dum.next

        # Time: O(n)
        # Space: O(1)

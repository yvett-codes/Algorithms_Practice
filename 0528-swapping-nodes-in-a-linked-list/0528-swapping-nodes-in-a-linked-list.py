# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pointA = pointB = head

        for i in range(k - 1):
            pointA = pointA.next
        cur = pointA

        while pointA.next:
            pointA = pointA.next
            pointB = pointB.next
        

        temp = pointB.val
        pointB.val = cur.val
        cur.val = temp

        return head
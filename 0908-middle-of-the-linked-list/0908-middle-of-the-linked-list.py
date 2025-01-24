# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        pointA = head

        while pointA.next:
            pointA = pointA.next
            length += 1
        pointA = head
        middle = length // 2
        
        for i in range(middle - 1):
            pointA = pointA.next

        return pointA.next

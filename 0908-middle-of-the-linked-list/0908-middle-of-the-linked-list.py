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
        middle = math.ceil(length/2)
        
        for i in range(middle - 1):
            pointA = pointA.next

        if length % 2 != 0:
            return pointA
        else:
            return pointA.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointA, pointB = l1, l2
        pointC = dum = ListNode()
        carry = 0

        while pointA or pointB:
            aVal = pointA.val if pointA else 0
            bVal = pointB.val if pointB else 0
            sum = aVal + bVal + carry
            if sum < 10:
                pointC.next = ListNode(sum)
                carry = 0
            else:
                sum -= 10
                pointC.next = ListNode(sum)
                carry = 1
            
            pointA = pointA.next if pointA else None
            pointB = pointB.next if pointB else None
            pointC = pointC.next

        pointC.next = ListNode(carry) if carry else None
        return dum.next
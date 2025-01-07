# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curA = l1
        curB = l2
        l3 = None
        carry = 0

        while curA or curB:
            curA_val = 0 if not curA else curA.val
            curB_val = 0 if not curB else curB.val
            to_add = curA_val + curB_val + carry

            if to_add > 9:
                to_add -= 10
                curC = ListNode(to_add)
                carry = 1
            else:
                curC = ListNode(to_add)
                carry = 0

            if not l3:
                l3 = curC
                prev = curC
            else:
                prev.next = curC
                prev = prev.next
            
            curA = curA.next if curA else None
            curB = curB.next if curB else None

        curC = curA if curA else curB
        prev.next = ListNode(carry) if carry else None
        return l3
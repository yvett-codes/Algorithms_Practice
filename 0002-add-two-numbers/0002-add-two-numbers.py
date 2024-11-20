# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        
        # convert
        num1 = ''
        while cur1:
            num1 += f"{cur1.val}"
            cur1 = cur1.next
        num1 = int(num1[::-1])

        num2 = ''
        while cur2:
            num2 += f"{cur2.val}"
            cur2 = cur2.next
        num2 = int(num2[::-1])
        
        # revert
        num3 = num1 + num2
        num3 = str(num3)
        num3 = num3[::-1]
        
        # build linked list
        l3_map = {}
        for i in range(len(num3)):
            l3_map[i] = ListNode(int(num3[i]))

        for key, value in l3_map.items():
            key += 1
            if key < len(num3):
                value.next = l3_map[key]
            else:
                value.next = None

        return l3_map[0]

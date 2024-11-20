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

        print(num1, type(num1))
        print(num2, type(num2))
        
        # revert
        num3 = num1 + num2
        print(num3, type(num3))
        num3 = str(num3)
        num3 = num3[::-1]
        
        # build linked list
        # how to loop to create a linked list? create a hash map of the nodes?
        # l3 = ListNode(num3[0]) if len(num3) < 2 else ListNode(num3[0])
        l3_map = {}
        for i in range(len(num3)):
            l3_map[i] = ListNode(int(num3[i]))
        print(l3_map)

        l3 = []
        for key, value in l3_map.items():
            key += 1
            # value.next = l3[key]
            # value.next = l3[key] if key < len(num3) - 1 else None
            if key < len(num3):
                value.next = l3_map[key]
            else:
                value.next = None
            # l3.append(l3_map[key])

        print(l3_map[0])
        return l3_map[0]

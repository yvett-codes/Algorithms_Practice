# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        if head != None:
            next_node = head.next
        else:
            return head
        prev_node = None

        while current_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            if next_node == None:
                head = prev_node
                return prev_node
            next_node = current_node.next
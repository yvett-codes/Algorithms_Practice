# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        1. Start at the beginning, iterate `k - 1` times to get a pointer at the left node
        2. To get the pointer on the right, calculate the length of the linked list, then iterate `length - k` times
        3. Then swap the two values
        '''
        pointL = pointR = head

        # Adjust left pointer
        for i in range(k - 1):
            pointL = pointL.next

        # Find length of input
        length = 1
        while pointR.next:
            pointR = pointR.next
            length += 1
        pointR = head

        # Adjust right pointer
        for i in range(length - k):
            pointR = pointR.next

        # Swap values
        rightVal = pointR.val
        leftVal = pointL.val
        pointL.val = rightVal
        pointR.val = leftVal

        return head
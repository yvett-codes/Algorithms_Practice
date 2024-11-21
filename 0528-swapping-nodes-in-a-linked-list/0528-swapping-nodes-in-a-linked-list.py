# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dum = ListNode()
        dum.next = head
        apple = banana = cherry = dum
        
        for i in range(k):
            cherry = apple
            apple = apple.next
        
        while apple.next:
            apple = apple.next
            banana = banana.next

        # switch
        if cherry.next == banana.next:
            return head
        
        # adjust the .nexts
        temp = cherry.next
        cherry.next = banana.next
        banana.next = temp
        
        # adjust the .next.nexts
        temp = cherry.next.next
        cherry.next.next = banana.next.next
        banana.next.next = temp

        return dum.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        cur = dum

        while list1 and list2:
            if list1.val < list2.val:
                #list1 is smaller
                cur.next = list1 # create the attachment
                # reset pointers
                cur = list1
                list1 = list1.next
            else:
                # list 2 is smaller
                cur.next = list2
                cur = list2
                list2 = list2.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dum.next
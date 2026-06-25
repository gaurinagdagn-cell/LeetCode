# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #edge case: empty list or single node
        if not head or not head.next or k == 0:
            return head
        
        # calc length of list and find the old tail
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
            
        # connect tail to the head
        old_tail.next = head
        
        # new tail (at index length - k - 1) 
        # and the new head (at index length - k)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        # break the circle
        new_tail.next = None
        
        return new_head
        
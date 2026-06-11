# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            # Save pointers
            nextPair = curr.next.next
            second = curr.next
            
            # Reverse the pair
            second.next = curr
            curr.next = nextPair
            prev.next = second
            
            # Update pointers for next iteration
            prev = curr
            curr = nextPair
            
        return dummy.next
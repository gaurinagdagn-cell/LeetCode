# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #  at least k nodes check
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next

        # reversing first k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # connecting with the rest of the list
        head.next = self.reverseKGroup(curr, k)

        return prev
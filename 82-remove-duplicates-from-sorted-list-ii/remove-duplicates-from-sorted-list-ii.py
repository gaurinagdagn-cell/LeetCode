# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            #check if curr node is the start of duplicates
            if curr.next and curr.val == curr.next.val:
                # skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # rmoving all duplicates
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next
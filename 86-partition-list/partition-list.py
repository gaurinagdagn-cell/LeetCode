# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy nodes for two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        # ptrs to build the two lists
        less = less_dummy
        greater = greater_dummy

        while head:
            if head.val < x:
                # adding node to the less than list
                less.next = head
                less = less.next
            else:
                # adding node to the >= list
                greater.next = head
                greater = greater.next

            head = head.next

        #end the greater list to avoid cycles
        greater.next = None

        # connecting the two lists
        less.next = greater_dummy.next

        return less_dummy.next
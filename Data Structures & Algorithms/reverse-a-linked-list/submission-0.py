# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            node = None
            while head.next is not None:
                node = ListNode(head.val, node)
                head = head.next
            node = ListNode(head.val, node)
            return node
        else:
            return None
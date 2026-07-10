# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_stack = []

        if head is None:
            return None

        while head.next:
            ptr = head.next
            node_stack.append(head)
            head.next = None
            head = ptr
        
        ptr = head
        while node_stack:
            ptr.next = node_stack.pop()
            ptr = ptr.next
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recursive(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        for _ in range(k):
            if not current:
                return head
            current = current.next
        
        prev = None
        current = head
        for _ in range(k):
            temporary = current.next
            current.next = prev
            prev = current
            current = temporary
        
        head.next = self.recursive(current, k)
        return prev
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.recursive(head, k)
        

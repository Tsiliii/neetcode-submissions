# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)

        before = dummy

        for _ in range(left-1):
            before = before.next
        
        endpoint = before.next
        current = endpoint
        prev = None

        for _ in range(right-left+1):
            temporary = current.next
            current.next = prev
            prev = current
            current = temporary

        before.next = prev
        endpoint.next = current

        return dummy.next
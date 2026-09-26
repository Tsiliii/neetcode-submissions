# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen = set()

        # while head:
        #     seen.add(head)
        #     if head.next and head.next in seen:
        #         return True            
        #     head = head.next
        # return False
        slow = head
        head = head

        while head and head.next:
            slow = slow.next
            head = head.next.next
            if head == slow:
                return True
        return False
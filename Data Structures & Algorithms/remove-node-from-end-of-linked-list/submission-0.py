# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def remover(self, node: Optional[ListNode], n: int) -> int:
        if not node:
            return n
        elif node:
            remaining = self.remover(node.next, n)
            if remaining > 0:
                return remaining - 1
            elif remaining == 0:
                node.next = node.next.next
                return -1
            else:
                return -1

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        self.remover(dummy, n)
        return dummy.next
        
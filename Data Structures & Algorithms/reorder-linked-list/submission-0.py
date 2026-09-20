# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while(node):
            temporary = node.next
            node.next = prev
            prev = node
            node = temporary
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = slow.next
        slow.next = None
        list2 = self.reverse(list2)

        while list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2
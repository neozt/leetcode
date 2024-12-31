from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next

        while current is not None:
            if current.next.val == 0:
                current = current.next.next
            else:
                current.val += current.next.val
                current.next = current.next.next

        return head
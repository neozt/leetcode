# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        beforeTarget = head
        tail = head
        for i in range(n):
            tail = tail.next

        if not tail:
            return head.next

        tail = tail.next

        while tail:
            beforeTarget = beforeTarget.next
            tail = tail.next


        beforeTarget.next = beforeTarget.next.next

        return head

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        oddHead = oddTail = head
        evenHead = evenTail = head.next

        isOdd = True
        current = evenHead.next

        while current:
            if isOdd:
                oddTail.next = current
                oddTail = oddTail.next
            else:
                evenTail.next = current
                evenTail = evenTail.next
            current = current.next
            isOdd = not isOdd

        evenTail.next = None
        oddTail.next = evenHead

        return oddHead

def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    print(result)
data = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ret = Solution().oddEvenList(data)

printList(ret)

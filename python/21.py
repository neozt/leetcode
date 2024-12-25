# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        current = new_list
        while list1 or list2:
            if list2 is None:
                current.next = list1
                list1 = list1.next
            elif list1 is None:
                current.next = list2
                list2 = list2.next
            elif list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        return new_list.next
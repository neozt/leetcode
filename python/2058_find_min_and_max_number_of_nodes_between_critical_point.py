# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        firstCriticalIndex = -1
        lastCriticalIndex = -1
        minDistance = float('inf')

        currentIndex = 0
        previous = None
        current = head

        while current is not None:
            if previous is not None and current.next is not None:
                is_minima = current.val < previous.val and current.val < current.next.val
                is_maxima = current.val > previous.val and current.val > current.next.val
                if is_minima or is_maxima:
                    if lastCriticalIndex != -1:
                       minDistance = min(minDistance, currentIndex - lastCriticalIndex)
                    if firstCriticalIndex == -1:
                        firstCriticalIndex = currentIndex

                    lastCriticalIndex = currentIndex

            currentIndex += 1
            previous = current
            current = current.next

        if firstCriticalIndex == lastCriticalIndex:
            return [-1, -1]

        return [minDistance, lastCriticalIndex - firstCriticalIndex]

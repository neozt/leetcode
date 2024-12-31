import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()

        heap = []
        for i, num in enumerate(nums):
            heap.append((num, i))
        heapq.heapify(heap)

        score = 0

        while heap:
            chosen_num, chosen_index = heapq.heappop(heap)
            if chosen_index in marked:
                continue

            score += chosen_num
            marked.add(chosen_index)
            marked.add(chosen_index - 1)
            marked.add(chosen_index + 1)

        return score


print(Solution().findScore([2,1,3,4,5,2]))
print(Solution().findScore([2,3,5,1,3,2]))

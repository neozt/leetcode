import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(-calculate_increment(pss,total), pss, total) for (pss, total) in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            (_, pss, total) = heapq.heappop(heap)
            heapq.heappush(heap, (-calculate_increment(pss + 1, total + 1), pss + 1, total + 1))

        total_pass_ratio = sum((pss / total) for (_, pss, total) in heap)
        return total_pass_ratio / len(classes)



def calculate_increment(pss, total):
    return ((pss + 1) / (total + 1)) - (pss/total)
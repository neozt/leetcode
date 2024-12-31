from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_elements = set(arr)
        unique_sorted = sorted(unique_elements)
        element_to_rank_map = {}
        for i in range(len(unique_sorted)):
            element_to_rank_map[unique_sorted[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = element_to_rank_map[arr[i]]

        return arr

print(Solution().arrayRankTransform([40,10,20,30]))
print(Solution().arrayRankTransform([100,100,100]))
print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))

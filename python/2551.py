from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairwise_sums = []
        for i in range(len(weights) - 1):
            pairwise_sums.append(weights[i] + weights[i + 1])
        pairwise_sums.sort()

        difference = 0
        for i in range(k - 1):
            difference += pairwise_sums[-(i + 1)] - pairwise_sums[i]

        return difference

print(Solution().putMarbles([1,3,5,1], 2))
print(Solution().putMarbles([1,3], 2))
print(Solution().putMarbles([1,4,2,5,2], 3))

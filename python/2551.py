from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairwise_sums = list(sorted(weights[i] + weights[i + 1] for i in range(n - 1)))

        difference = 0
        for i in range(k - 1):
            difference += pairwise_sums[-(i + 1)] - pairwise_sums[i]

        return difference

print(Solution().putMarbles([1,3,5,1], 2))
print(Solution().putMarbles([1,3], 2))
print(Solution().putMarbles([1,4,2,5,2], 3))

import math
from typing import List

# k = 3
# [1,3,5,1,1,3,5,1]


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        def helper(start: int, k_left: int) -> tuple[int, int]:
            if k_left == 1:
                only_option = weights[start] + weights[-1]
                return only_option, only_option

            best_min = math.inf
            best_max = -math.inf
            for end in range(start, len(weights) - k_left + 1):
                curr_min, curr_max = helper(end + 1, k_left - 1)
                best_min = min(best_min, curr_min + weights[start] + weights[end])
                best_max = max(best_max, curr_max + weights[start] + weights[end])

            return best_min, best_max

        minimum, maximum = helper(0, k)
        return maximum - minimum

# print(Solution().putMarbles([1,3,5,1], 2))
# print(Solution().putMarbles([1,3], 2))
print(Solution().putMarbles([1,4,2,5,2], 3))

from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        longest = 0
        for i in range(len(candidates)):
            curr = candidates[i]
            for j in range(i + 1, len(candidates)):
                curr = curr & candidates[j]
                if curr == 0:
                    break
                longest = max(longest, j-i + 1)
        return longest


print(Solution().largestCombination([16, 17, 71, 62, 12, 24, 14]))
print(Solution().largestCombination([8, 8]))

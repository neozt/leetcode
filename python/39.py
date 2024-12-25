from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.recursive(candidates, [], target)


    def recursive(self, candidates, accumulator, target):
        if target < 0:
            # Already negative, no more answers to be found
            return []

        if target == 0:
            return [accumulator]

        if not candidates:
            # No more options to try, no more answers to be found
            return []

        # We have two options here, either we include the first candidate or we don't
        include_self = self.recursive(candidates, accumulator + [candidates[0]], target - candidates[0])
        exclude_self = self.recursive(candidates[1:], accumulator, target)

        return include_self + exclude_self


print(Solution().combinationSum([2, 3, 6, 7], 7))
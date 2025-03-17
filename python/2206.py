from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        unmatched = set()
        for num in nums:
            if num in unmatched:
                unmatched.remove(num)
            else:
                unmatched.add(num)

        return len(unmatched) == 0
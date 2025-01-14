from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        freq = Counter(nums)
        nums_sorted = sorted(freq.keys())

        for n in nums_sorted:
            if freq[n]:
                count = freq[n]
                for i in range(n, n + k):
                    freq[i] -= count
                    if freq[i] < 0:
                        return False

        return True

print(Solution().isPossibleDivide([1,2,3,3,4,4,5,6], 4))
print(Solution().isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3))
print(Solution().isPossibleDivide([1,2,3,4], 3))
print(Solution().isPossibleDivide([16,21,26,35], 4))

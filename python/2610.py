from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter()

        result = []

        for num in nums:
            if freq[num] >= len(result):
                result.append([])

            result[freq[num]].append(num)
            freq[num] += 1

        return result


assert Solution().findMatrix([1,3,4,1,2,3,1]) == [[1, 3, 4, 2], [1, 3], [1]]
assert Solution().findMatrix([1,2,3,4]) == [[1, 2, 3, 4]]
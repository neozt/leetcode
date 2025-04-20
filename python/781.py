import math
from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)

        result = 0
        for num, f in freq.items():
            group_size = num + 1
            groups = math.ceil(f / group_size)
            result += group_size * groups

        return result

print(Solution().numRabbits([1,1,2]))
print(Solution().numRabbits([10, 10, 10]))
print(Solution().numRabbits([1,0,1,0,0]))

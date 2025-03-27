from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        x, f = find_dominant(nums)

        f1 = 0
        for i, num in enumerate(nums[0:-1]):
            if num == x:
                f1 += 1

            f2 = f - f1
            if (f1 > (i + 1) // 2) and (f2 > (len(nums) - i - 1) // 2):
                return i

        return -1


def find_dominant(nums: List[int]) -> tuple[int, int]:
    counter = Counter(nums)

    for num, count in counter.items():
        if count > len(nums) // 2:
            return num, count

    raise Exception

print(Solution().minimumIndex([1,2,2,2]))
print(Solution().minimumIndex([2,1,3,1,1,1,7,1,2,1]))
print(Solution().minimumIndex([3,3,3,3,7,2,2]))

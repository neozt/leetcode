from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0

        for num in nums:
            mask ^= 1 << num

        print( "{0:b}".format(num))



print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
# print(Solution().singleNumber([-1, 0]))
print(Solution().singleNumber([1, 0]))

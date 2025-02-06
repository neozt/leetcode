import math
from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                freq[product] += 1

        result = 0
        for count in freq.values():
            # We have `count` groups, any two of them will form a valid "pair".
            # We multiply by 2 twice because given a * b = c * d, a and b, and c and d are interchangeable
            result += math.perm(count, 2) * 2 * 2

        return result


print(Solution().tupleSameProduct([2,3,4,6]))
print(Solution().tupleSameProduct([1,2,4,5,10]))
print(Solution().tupleSameProduct([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]))

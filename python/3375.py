from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set()
        for num in nums:
            if num < k:
                return -1
            unique.add(num)

        if k in unique:
            unique.remove(k)

        return len(unique)

print(Solution().minOperations([5,2,5,4,5], 2))
print(Solution().minOperations([2,1,2], 2))
print(Solution().minOperations([9,7,5,3], 2))

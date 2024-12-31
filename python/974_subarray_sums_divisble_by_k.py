from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        prefix_map = {0: 1}

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            mod = prefix_sum if prefix_sum >= 0 else prefix_sum + k
            if mod in prefix_map:
                result += prefix_map[mod]
                prefix_map[mod] += 1
            else:
                prefix_map[mod] = 1

        return result

print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
print(Solution().subarraysDivByK([5], 9))

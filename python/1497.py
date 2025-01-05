from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_counter = Counter()
        for num in arr:
            mod_counter[num % k] += 1

        if mod_counter[0] % 2 != 0:
            return False

        for i in range(1, (k // 2) + 1):
            if mod_counter[i] != mod_counter[k - i]:
                return False

        return True

print(Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5))
print(Solution().canArrange([1,2,3,4,5,6], 7))
print(Solution().canArrange([1,2,3,4,5,6], 10))
print(Solution().canArrange([-1,-1,-1,-1,2,2,-2,-2], 3))

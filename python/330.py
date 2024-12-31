from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        result = 0
        cs = self.combination_sums(nums, n)
        while not all(cs):
            for i in range(n + 1):
                if not cs[i]:


    def combination_sums(self, nums, n):
        result = [False] * (n + 1)

        def helper(i, acc):
            if acc > n:
                return
            if i == len(nums):
                result[acc] = True
                return

            helper(i + 1, acc + nums[i])
            helper(i + 1, acc)

        helper(0, 0)

        return result


Solution().minPatches([1, 3], 6)
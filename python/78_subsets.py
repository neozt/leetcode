from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(temp_list, start):
            if (start == len(nums)):
                result.append(temp_list[:])
                return

            temp_list.append(nums[start])
            backtrack(temp_list, start + 1)
            temp_list.pop()
            backtrack(temp_list, start + 1)

        backtrack([], 0)
        return result

print(Solution().subsets([1, 2, 3]))
print(Solution().subsets([0]))
print(Solution().subsets([]))

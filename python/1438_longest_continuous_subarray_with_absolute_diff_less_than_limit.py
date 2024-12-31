from collections import defaultdict, deque
from typing import List


class Solution(object):
    def longestSubarray(self, nums, limit):
        increase = deque()
        decrease = deque()
        max_length = 0
        left = 0

        for right in range(len(nums)):
            while increase and nums[right] < increase[-1]:
                increase.pop()
            increase.append(nums[right])

            while decrease and nums[right] > decrease[-1]:
                decrease.pop()
            decrease.append(nums[right])

            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.popleft()
                if nums[left] == decrease[0]:
                    decrease.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


# print(Solution().longestSubarray([8, 2, 4, 7], 4))
print(Solution().longestSubarray([10,1,2,4,7,2], 5))
# print(Solution().longestSubarray([4,2,2,2,4,4,2,2], 0))

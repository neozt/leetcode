from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_elements = len(set(nums))

        left, right = -1, -1
        counter = {}
        result = 0
        while left < len(nums) - 1:
            while right < len(nums) - 1 and len(counter) < distinct_elements:
                right += 1
                right_element = nums[right]

                if right_element in counter:
                    counter[right_element] += 1
                else:
                    counter[right_element] = 1

            if len(counter) == distinct_elements:
                result += len(nums) - right

            left += 1
            left_element = nums[left]
            if counter[left_element] == 1:
                del counter[left_element]
            else:
                counter[left_element] -= 1

        return result

print(Solution().countCompleteSubarrays([1,3,1,2,2]))
print(Solution().countCompleteSubarrays([5,5,5,5]))


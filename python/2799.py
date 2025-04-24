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
                increment_counter(counter, nums[right])

            if len(counter) < distinct_elements:
                break

            result += len(nums) - right
            left += 1
            decrement_counter(counter, nums[left])

        return result

def increment_counter(counter, element):
    if element not in counter:
        counter[element] = 1
    else:
        counter[element] += 1

def decrement_counter(counter, element):
    if counter[element] == 1:
        del counter[element]
    else:
        counter[element] -= 1


print(Solution().countCompleteSubarrays([1,3,1,2,2]))
print(Solution().countCompleteSubarrays([5,5,5,5]))


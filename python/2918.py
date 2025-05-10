from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1 = 0
        zero_count_1 = 0
        sum_2 = 0
        zero_count_2 = 0

        for num in nums1:
            sum_1 += num
            zero_count_1 += 1 if num == 0 else 0

        for num in nums2:
            sum_2 += num
            zero_count_2 += 1 if num == 0 else 0

        min_sum_1 = sum_1 + zero_count_1
        min_sum_2 = sum_2 + zero_count_2

        # We define nums1 as our target array, which has the larger min_sum. Swap as necessary
        if min_sum_2 > min_sum_1:
            min_sum_1, min_sum_2 = min_sum_2, min_sum_1
            sum_1, sum_2 = sum_2, sum_1
            zero_count_1, zero_count_2 = zero_count_2, zero_count_1

        if min_sum_1 != min_sum_2 and zero_count_2 == 0:
            return -1

        return min_sum_1

print(Solution().minSum([3,2,0,1,0], [6,5,0]))
print(Solution().minSum([2,0,2,0], [1,4]))

from typing import List, Callable


class Solution:
    def maximumCount(self, nums: List[int]):
        bisect_right = lambda x: bisect(x, lambda arr, idx : arr[idx] > 0)
        bisect_left = lambda x: bisect(x, lambda arr, idx : arr[idx] >= 0)

        pos = len(nums) - bisect_right(nums)
        neg = bisect_left(nums)

        return max(pos, neg)

def bisect(nums: List[int], condition: Callable[[List[int], int], bool]):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if condition(nums, mid):
            right = mid
        else:
            left = mid + 1
    return left

print(Solution().maximumCount([-2,-1,-1,1,2,3]))
print(Solution().maximumCount([-3,-2,-1,0,0,1,2]))
print(Solution().maximumCount([5,20,66,1314]))

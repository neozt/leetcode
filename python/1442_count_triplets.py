from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr) - 1):
            a = arr[i]

            for j in range(i + 1, len(arr)):
                b = 0

                if j > i + 1:
                    a ^= arr[j - 1]

                for k in range(j, len(arr)):
                    b ^= arr[k]

                    if a == b:
                        result += 1

        return result


print(Solution().countTriplets([2, 3, 1, 6, 7]))
print(Solution().countTriplets([1, 1, 1, 1, 1]))
print(Solution().countTriplets([2,3]))
print(Solution().countTriplets([2,3,1,6,7]))



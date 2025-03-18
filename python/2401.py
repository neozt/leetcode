from typing import List, Set


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def convert_to_bit_set(num: int) -> Set[int]:
            index = 0
            result = set()
            while num:
                if num & 1:
                    result.add(index)

                index += 1
                num = num >> 1

            return result

        bit_sets = [convert_to_bit_set(num) for num in nums]

        longest = 0
        for i in range(len(bit_sets)):
            seen = set()
            for j in range(i, len(bit_sets)):
                current = bit_sets[j]
                if seen.intersection(current):
                    break

                seen = seen.union(current)
                longest = max(longest, j - i + 1)

        return longest


print(Solution().longestNiceSubarray([1,3,8,48,10]))
print(Solution().longestNiceSubarray([3,1,5,11,13]))

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])

        length = len(colors)
        l = 0
        r = 1
        result = 0

        while r < length:
            if colors[r] == colors[r - 1]:
                l = r
                r += 1
            else:
                if r - l + 1 >= k:
                    result += 1

                r += 1

        return result

print(Solution().numberOfAlternatingGroups([0,1,0,1,0], 3))
print(Solution().numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))
print(Solution().numberOfAlternatingGroups([1,1,0,1], 4))




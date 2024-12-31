from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = map(lambda x: x[1], sorted(zip(heights, names), reverse=True))
        return list(result)


print(Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
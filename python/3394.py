from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        sorted_horizontal = sorted(rectangles, key = lambda x: x[0])
        sorted_vertical = sorted(rectangles, key = lambda x: x[1])

        current = sorted_horizontal[0][2]
        cuts = 0
        for rectangle in sorted_horizontal[1:]:
            if current <= rectangle[0]:
                cuts += 1
                if cuts == 2:
                    return True

            current = max(current, rectangle[2])

        current = sorted_vertical[0][3]
        cuts = 0
        for rectangle in sorted_vertical[1:]:
            if current <= rectangle[1]:
                cuts += 1
                if cuts == 2:
                    return True

            current = max(current, rectangle[3])

        return False

print(Solution().checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(Solution().checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
print(Solution().checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))

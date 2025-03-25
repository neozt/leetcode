from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_valid_slice(rectangles: List[List[int]], extract_start, extract_end):
            rectangles.sort(key = extract_start)

            current = extract_end(rectangles[0])
            cuts = 0
            for rectangle in rectangles[1:]:
                if current <= extract_start(rectangle):
                    cuts += 1
                    if cuts == 2:
                        return True

                current = max(current, extract_end(rectangle))

            return False

        # int -> List -> any
        def array_accessor(i: int):
            def accessor(arr: List):
                return arr[i]
            return accessor

        return can_valid_slice(rectangles, array_accessor(0), array_accessor(2)) or can_valid_slice(rectangles, array_accessor(1), array_accessor(3))

print(Solution().checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(Solution().checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
print(Solution().checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))

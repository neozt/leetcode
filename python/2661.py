from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        num_to_coord = [(-1, -1) for _ in range((m * n) + 1)]

        for r in range(m):
            for c in range(n):
                num_to_coord[mat[r][c]] = (r,c)

        row_count = [0] * m
        col_count = [0] * n

        for i, num in enumerate(arr):
            r, c = num_to_coord[num]
            row_count[r] += 1
            col_count[c] += 1

            if row_count[r] == n or col_count[c] == m:
                return i

        raise Exception

print(Solution().firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]))
print(Solution().firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]))
print(Solution().firstCompleteIndex([1,4,5,2,6,3], [[4,3,5],[1,2,6]]))


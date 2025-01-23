from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        first_in_row = [None] * m
        first_in_col = [None] * n

        result = set()

        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    continue


                if first_in_row[r] is None:
                    first_in_row[r] = (r,c)
                else:
                    result.add((r,c))
                    result.add(first_in_row[r])

                if first_in_col[c] is None:
                    first_in_col[c] = (r,c)
                else:
                    result.add((r,c))
                    result.add(first_in_col[c])

        return len(result)

print(Solution().countServers([[1,0],[0,1]]))
print(Solution().countServers([[1,0],[1,1]]))
print(Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))

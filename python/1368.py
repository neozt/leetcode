import math
from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0),
        }

        m = len(grid)
        n = len(grid[0])

        q = deque([(0, 0, 0)])
        min_cost = { (0,0): 0 }

        while q:
            r, c, cost = q.popleft()
            if r == m - 1 and c == n - 1:
                return cost

            for d in directions:
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc
                n_cost = cost if d == grid[r][c] else cost + 1

                if (
                    nr < 0 or nc < 0 or nr >= m or nc >= n or n_cost >= min_cost.get((nr, nc), math.inf)
                ):
                    continue

                min_cost[(nr, nc)] = n_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))


        raise Exception()


print(Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
print(Solution().minCost([[1,1,3],[3,2,2],[1,1,4]]))
print(Solution().minCost([[1,2],[4,3]]))

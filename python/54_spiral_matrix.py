from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        result = []
        visited = set()

        def dfs(current_position: tuple[int, int], current_direction: int):
            x, y = current_position
            # Check if out of bounds
            if not 0 <= x < rows:
                return
            if not 0 <= y < cols:
                return

            # Check if already visited
            if current_position in visited:
                return

            # Visit this node
            visited.add(current_position)
            result.append(matrix[x][y])

            for i in range(4):
                # Visit neighbouring nodes in correct order
                next_direction = (current_direction + i) % len(DIRECTIONS)
                next_position = (x + DIRECTIONS[next_direction][0], y + DIRECTIONS[next_direction][1])
                dfs(next_position, next_direction)

        dfs((0, 0), 0)

        return result


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = [[False] * cols for i in range(rows)]

        def dfs(row_index, col_index, target, visited):
            if not target:
                return True

            if not 0 <= row_index < rows or not 0 <= col_index < cols or visited[row_index][col_index]:
                return False

            if board[row_index][col_index] != target[0]:
                return False

            visited[row_index][col_index] = True

            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if dfs(row_index + x, col_index + y, target[1:], visited):
                    return True

            visited[row_index][col_index] = False # backtrack

            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word, visited):
                    return True

        return False


# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))

board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
print(sum(board, []))
# print(Solution().exist(board, "ABCESEEEFS"))

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        is_safe = [None] * n
        visited = [False] * n

        def dfs(num: int) -> bool:
            if not graph[num]:
                # Terminal node
                is_safe[num] = True
                return True

            if visited[num]:
                # Cycle detected
                is_safe[num] = False
                return False

            if is_safe[num] is not None:
                return is_safe[num]

            visited[num] = True
            is_num_safe = all(dfs(neighbor) for neighbor in graph[num])
            visited[num] = False

            is_safe[num] = is_num_safe

            return is_num_safe

        result = []
        for i in range(n):
            safe = dfs(i)
            if safe:
                result.append(i)

        return result

print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))


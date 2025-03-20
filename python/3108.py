from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

    def union(self, u: int, v: int):
        self.parent[self.find(u)] = self.find(v)


    def find(self, u: int):
        while self.parent[u] != self.parent[self.parent[u]]:
            self.parent[u] = self.parent[self.parent[u]]
        return self.parent[u]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)

        for u, v, w in edges:
            uf.union(u, v)

        group_cost = [None] * n

        for u, v, w in edges:
            parent = uf.find(u)
            current_cost = group_cost[parent] if group_cost[parent] is not None else w
            new_cost = current_cost & w
            group_cost[parent] = new_cost

        result = []
        for u, v in query:
            if uf.find(u) != uf.find(v):
                result.append(-1)
            else:
                result.append(group_cost[uf.find(u)])

        return result


print(Solution().minimumCost(5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]]))
print(Solution().minimumCost(5, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]))

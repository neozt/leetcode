from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.group_cost: List[int | None] = [None] * n
        self.rank = [1] * n

    def union(self, u: int, v: int, w: int):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if self.rank[parent_u] > self.rank[parent_v]:
            self.rank[parent_u] += self.rank[parent_v]
        else:
            self.rank[parent_v] += self.rank[parent_u]
            parent_u, parent_v = parent_v, parent_u

        self.parent[parent_v] = parent_u
        cost = w
        if self.group_cost[parent_u] is not None:
            cost &= self.group_cost[parent_u]
        if self.group_cost[parent_v] is not None:
            cost &= self.group_cost[parent_v]
        self.group_cost[parent_u] = cost

    def find(self, u: int):
        while self.parent[u] != self.parent[self.parent[u]]:
            self.parent[u] = self.parent[self.parent[u]]
        return self.parent[u]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)

        for u, v, w in edges:
            uf.union(u, v, w)

        result = []
        for u, v in query:
            parent_u = uf.find(u)
            if parent_u != uf.find(v):
                result.append(-1)
            else:
                result.append(uf.group_cost[parent_u])

        return result


print(Solution().minimumCost(5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]]))
print(Solution().minimumCost(5, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]))
print(Solution().minimumCost(4, [[2,3,1],[1,3,5],[1,2,6],[3,0,7],[1,3,7],[0,2,5],[0,1,7]], [[2,1],[1,2],[0,1],[2,0],[0,2],[1,2],[3,2],[0,3],[2,1],[1,2]]))

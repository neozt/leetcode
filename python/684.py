from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def __repr__(self):
        return str(self.parent)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            node1, node2 = edge

            if uf.find(node1) == uf.find(node2):
                return edge
            uf.union(node1, node2)
        raise Exception()


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

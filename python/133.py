# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        return dfs_cloner(node, {})


def dfs_cloner(node, cloned):
    if node in cloned:
        return cloned[node]

    # Clone node and add to dictionary
    clone = Node(node.val, [])
    cloned[node] = clone

    # Append clones of node's neighbors to node's neighbors list.
    for neighbor in node.neighbors:
        neighbor_clone = (dfs_cloner(neighbor, cloned))
        clone.neighbors.append(neighbor_clone)

    return clone


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neightbors = [node2, node4]
node4.neighbors = [node3, node1]

clone = Solution().cloneGraph(node1)


print(node1)
print(node2)
print(node3)
print(node4)
print(node1.neighbors)
print(clone)
print(clone.neighbors)

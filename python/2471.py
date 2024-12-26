# TODO complete this

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def map_to_val(tree_nodes):
    return list(node.val for node in tree_nodes)

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        rows = []
        current_level = [root]
        while current_level:
            rows.append(current_level)
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level

        result = 0
        for row in rows:
            values = map_to_val(row)
            correct_sequence = sorted(values)

            value_to_index_map = {}
            for i, v in enumerate(values):
                value_to_index_map[v] = i

            for i, expected_val in enumerate(correct_sequence):
                actual_val = values[i]
                if actual_val != expected_val:
                    result += 1
                    correct_index = value_to_index_map[actual_val]
                    values[i], values[correct_index] = values[correct_index], values[i]
                    value_to_index_map[actual_val] = i
                    value_to_index_map[expected_val] = correct_index

        return result



node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)

node_2 = TreeNode(2, node_5, node_4)
node_3 = TreeNode(3, node_7, node_6)

root = TreeNode(1, node_3, node_2)

print(Solution().minimumOperations(root))














# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, level = [], [ root ]
        while level:
            values = []
            next_level = []
            for node in level:
                if (node):
                    values.append(node.val)
                    next_level.extend([node.left, node.right])
            if values:
                result.append(values)

            level = next_level

        return result

input = TreeNode(
    3,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)

print(Solution().levelOrder(input))
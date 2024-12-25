# Definition for a binary tree node.
import math
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        current_level = [root]
        result = []
        while current_level:
            next_level = []
            best = -math.inf
            for node in current_level:
                best = max(best, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(best)
            current_level = next_level

        return result
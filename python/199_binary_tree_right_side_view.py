# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        current_level = [root]
        result = []
        while current_level:
            result.append(current_level[-1].val)
            next_level = []
            for node in current_level:
                for child in node.left, node.right:
                    if child:
                        next_level.append(child)

            current_level = next_level

        return result

Solution().rightSideView()
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        helper(root.left, root.right, 0)

        return root



def helper(left: Optional[TreeNode], right: Optional[TreeNode], level):
    if not left or not right:
        return None

    if level % 2 == 0:
        left.val, right.val = right.val, left.val

    helper(left.left, right.right, level + 1)
    helper(left.right, right.left, level + 1)
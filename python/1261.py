# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.buildTree(root, None, None)

    def find(self, target: int) -> bool:
        return target in self.values

    def buildTree(self, node: TreeNode, left_parent_value: Optional[int], right_parent_value: Optional[int]) -> None:
        if not node:
            return

        if left_parent_value is None and right_parent_value is None:
            value = 0
        elif left_parent_value is not None:
            value = left_parent_value * 2 + 1
        else:
            value = right_parent_value * 2 + 2

        self.values.add(value)
        self.buildTree(node.left, value, None)
        self.buildTree(node.right, None, value)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
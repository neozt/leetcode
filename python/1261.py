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
        self.buildTree(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

    def buildTree(self, node: TreeNode, value) -> None:
        if not node:
            return

        self.values.add(value)
        self.buildTree(node.left, value * 2 + 1)
        self.buildTree(node.right, value * 2 + 2)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
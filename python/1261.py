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

        if not root:
            return

        self.values.add(0)
        self.buildTree(root.left, 0, None)
        self.buildTree(root.right, None, 0)


    def find(self, target: int) -> bool:
        return target in self.values

    def buildTree(self, node: TreeNode, leftParentValue: Optional[int], rightParentValue: Optional[int]) -> None:
        if not node:
            return

        value = 2 * rightParentValue + 2 if leftParentValue is None else 2 * leftParentValue + 1
        self.values.add(value)
        self.buildTree(node.left, value, None)
        self.buildTree(node.right, None, value)





# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
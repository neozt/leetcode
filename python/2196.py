# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        map = defaultdict(TreeNode)
        root = None
        for parent, child, isLeft in descriptions:
            parentNode = map[parent]
            parentNode.val = parent
            childNode = map[child]
            childNode.val = child
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            if not root or root.val == child:
                root = parentNode

        return root


print(Solution().createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]).val)
print(Solution().createBinaryTree([[1,2,1],[2,3,0],[3,4,1]]).val)

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = deque([(root, 0)])
        max_width = 0

        while level:
            _, left = level[0]
            _, right = level[-1]
            max_width = max(max_width, right - left + 1)

            level_length = len(level)

            for i in range(level_length):
                node, pos = level.popleft()
                if node.left:
                    level.append((node.left, pos * 2))
                if node.right:
                    level.append((node.right, pos * 2 + 1))

        return max_width

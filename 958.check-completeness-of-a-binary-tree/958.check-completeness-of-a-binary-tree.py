from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([(root, 1)])
        count = 0
        while queue:
            node, num = queue.popleft()
            count += 1
            if num != count:
                return False
            if node.left:
                queue.append((node.left, num * 2))
            if node.right:
                queue.append((node.right, num * 2 + 1))
        return True
    
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
f = TreeNode(5)
e = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = f
# c.right = e

s = Solution()
print(s.isCompleteTree(a))

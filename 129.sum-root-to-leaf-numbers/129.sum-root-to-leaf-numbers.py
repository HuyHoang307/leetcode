from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], total: int) -> int:
            if not node:
                return 0
            total = total * 10 + node.val
            if not node.left and not node.right:
                return total
            return dfs(node.left, total) + dfs(node.right, total)
        
        return dfs(root, 0)
    
a = TreeNode(4)
b = TreeNode(9)
c = TreeNode(0)
d = TreeNode(5)
f = TreeNode(1)
a.right = c
a.left = b
b.left = f
b.right = d
s = Solution()
print(s.sumNumbers(a))
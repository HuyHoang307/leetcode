from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, direction, cnt):
            if not node:
                if cnt-1 > self.ans:
                    self.ans = cnt -1
                return cnt-1

            if direction == "left":
                dfs(node.right, "right", cnt + 1)
                dfs(node.left, "left", 1)
            else:
                dfs(node.left, "left", cnt + 1)
                dfs(node.right, "right", 1)
            return 
        
        if not root.left and not root.right:
            return 0

        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)
        return self.ans

        
        
            
            
            
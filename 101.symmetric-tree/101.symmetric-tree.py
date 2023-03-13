from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        if not root:
            return True
        return isMirror(root.left, root.right)

root = TreeNode(1)
ar = TreeNode(2)
al = TreeNode(2)
bl = TreeNode(3)
br = TreeNode(3)
cl = TreeNode(4)
cr = TreeNode(4)
root.left = al
root.right = ar
al.left = bl
al.right = cl
ar.right = br
ar.left = cr

s = Solution()
print(s.isSymmetric(root))
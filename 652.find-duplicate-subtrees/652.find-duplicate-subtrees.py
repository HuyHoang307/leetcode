from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        hash_table = {}
        def recursion(node: Optional[TreeNode]):
            if not node:
                return '#'
            left = recursion(node.left)
            right = recursion(node.right)
            sub_tree = left + ',' + right + ',' + str(node.val)
            if sub_tree not in hash_table:
                hash_table[sub_tree] = 1
            elif hash_table[sub_tree] == 1:
                res.append(node)
                hash_table[sub_tree] = 0
            return sub_tree
        recursion(root)
        return res

        


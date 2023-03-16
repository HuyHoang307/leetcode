from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(inorder_start, inorder_end, postorder_start, postorder_end):
            if inorder_start > inorder_end:
                return None

            val = postorder[postorder_end]
            root = TreeNode(val)
            inorder_index = inorder_dict[val]
            left_tree_size = inorder_index - inorder_start

            root.left = buildTreeHelper(inorder_start, inorder_index-1, postorder_start, postorder_start+left_tree_size-1)
            root.right = buildTreeHelper(inorder_index+1, inorder_end, postorder_start+left_tree_size, postorder_end-1)

            return root
        
        n = len(inorder)
        inorder_dict = {val: i for i, val in enumerate(inorder)}
        return buildTreeHelper(0, n-1, 0, n-1)



inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

s = Solution()
root = s.buildTree(inorder, postorder)

queue = [root]
while len(queue):
    node = queue.pop(0)
    if not node:
        print('null', end=' ,')
    else:
        print(node.val, end=' ,')
        queue.append(node.left)
        queue.append(node.right)
    
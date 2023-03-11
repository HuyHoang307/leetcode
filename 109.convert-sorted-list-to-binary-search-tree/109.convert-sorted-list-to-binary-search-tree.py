from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next))


a = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
s = Solution()
root = s.sortedListToBST(a)
def printTree(root):
    queue = [root]
    while len(queue):
        node = queue.pop(0)
        print(node.val if node else 'null', end=', ')
        if node:
            queue.append(node.left)
            queue.append(node.right)
printTree(root)

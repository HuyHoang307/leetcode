from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = last = head
        for _ in range(1, k):
            first = first.next

        null_checker = first
        while null_checker.next:
            last = last.next
            null_checker = null_checker.next
        first.val, last.val = last.val, first.val
        return head


head_val = [1, 2, 3, 4, 5]
n = len(head_val)
start = head = ListNode(head_val[0])
for i in range(1, n):
    start.next = ListNode(head_val[i])
    start = start.next

k = 2
s = Solution()
print(s.swapNodes(head, k))

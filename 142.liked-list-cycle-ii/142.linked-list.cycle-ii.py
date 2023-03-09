from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mem = defaultdict(list)
        while head:
            for node in mem[head.val]:
                if head is node:
                    return node
            mem[head.val].append(head)
            head = head.next
        

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b

s = Solution()
print(s.detectCycle(a).val)
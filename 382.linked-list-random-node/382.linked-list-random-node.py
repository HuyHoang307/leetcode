from typing import Optional
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    arr = []

    def __init__(self, head: Optional[ListNode]):
        self.arr.clear()
        self.length = 0
        while head:
            self.arr.append(head.val)
            self.length += 1
            head = head.next
        

    def getRandom(self) -> int:
        choice = int(random.random() * self.length)
        return self.arr[choice]

        


# Your Solution object will be instantiated and called as such:
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
obj = Solution(a)
print(obj.arr)
for i in range(10):
    print(obj.getRandom())
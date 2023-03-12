from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        
        heap = []
        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))
        
        heapq.heapify(heap)
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next


lists = [
    ListNode(1, ListNode(2, ListNode(3))),
    ListNode(4, ListNode(5, ListNode(6, ListNode(7))))
]

lists2 = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
lists3 = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(0, ListNode(2))
]
s = Solution()
a = s.mergeKLists(lists3)
while a:
    print(a.val)
    a = a.next
            


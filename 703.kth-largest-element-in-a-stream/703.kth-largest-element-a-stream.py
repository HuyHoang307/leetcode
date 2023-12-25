import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        if val <= self.nums[-1]:
            return self.nums[-1]
        self.nums.pop()
        left, right = 0, self.k - 2
        while left < right:
            mid = (left + right) // 2
            if self.nums[mid] == val:
                return mid
            elif self.nums[mid] < val:
                left = mid + 1
            else:
                right = mid - 1

        self.nums.insert(val, left)
        return self.nums[-1]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))

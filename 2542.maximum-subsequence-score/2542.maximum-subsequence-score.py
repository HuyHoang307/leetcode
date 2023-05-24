from heapq import heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1, nums2, k):
        total = res = 0
        heap = []

        pairs = zip(nums1, nums2)

        sorted_pairs = sorted(pairs, key=lambda x: -x[1])

        for pair in sorted_pairs:
            num1, num2 = pair
            heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(res, total * num2)

        return res


nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
s = Solution()
print(s.maxScore(nums1, nums2, k))

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
        return -stones[0]


stones = [2, 7, 4, 1, 8, 1]
s = Solution()
print(s.lastStoneWeight(stones))

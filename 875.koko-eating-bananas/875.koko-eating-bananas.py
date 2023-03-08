from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int):
            res = 0
            for pile in piles:
                res += ceil(pile / k)
            return res <= h
        low, high = 1, max(piles)
        while high > low:
            mid = (high + low) >> 1
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low
                

piles = [3,6,7,11]
h = 8
s = Solution()
print(s.minEatingSpeed(piles, h))

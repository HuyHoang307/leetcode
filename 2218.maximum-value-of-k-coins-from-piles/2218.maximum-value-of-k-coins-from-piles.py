from functools import lru_cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:
        N = len(piles)

        @lru_cache(None)
        def f(i, k):
            if i == N:
                return 0
            res, s = f(i + 1, k), 0
            for j in range(min(k, len(piles[i]))):
                s += piles[i][j]
                k -= 1
                res = max(res, s + f(i + 1, k))
            return res

        return f(0, K)
    

piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
k = 7
s = Solution()
print(s.maxValueOfCoins(piles,k))
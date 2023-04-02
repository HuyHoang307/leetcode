from bisect import bisect_left
from math import ceil
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len (potions)
        potions.sort()
        R = []
        for s in spells:
            n = ceil(success / s)
            R.append(m - bisect_left(potions, n))

        return R

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

s = Solution()
print(s.successfulPairs(spells, potions, success))
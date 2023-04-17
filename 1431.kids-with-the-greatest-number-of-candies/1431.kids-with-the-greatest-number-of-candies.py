from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [i + extraCandies >= maxCandies for i in candies]

candies = [2,3,5,1,3]
extraCandies = 3
s = Solution()
print(s.kidsWithCandies(candies, extraCandies))

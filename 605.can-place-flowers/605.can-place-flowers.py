from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros, ans = 1, 0  
        for plot in flowerbed:
            if plot == 0: 
                zeros += 1
            else:
                ans += (zeros - 1) // 2
                zeros = 0
        return ans + zeros // 2 >= n 



flowerbed = [1,0,0,0,1,0,0]
n = 2

s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
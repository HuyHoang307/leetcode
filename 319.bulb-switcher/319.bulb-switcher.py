from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
    
n = 10**9
s = Solution()
print(s.bulbSwitch(n))
            
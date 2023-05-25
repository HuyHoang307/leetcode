from functools import lru_cache


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (k + maxPts)

        for i in range(k, min(n + 1, k + maxPts)):
            dp[i] = 1.0

        s = min(n - k + 1, maxPts)
        for j in range(k - 1, -1, -1):
            dp[j] = s/float(maxPts)
            s += dp[j] - dp[j + maxPts]

        return dp[0]


n = 21
k = 17
maxPts = 10
s = Solution()
print(s.new21Game(n, k, maxPts))
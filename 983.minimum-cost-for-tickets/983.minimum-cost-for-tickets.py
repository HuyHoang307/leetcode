from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (days[n-1]+1)
        for i in range(1, days[n-1]+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        return dp[days[n-1]]


    
days = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29]
costs = [3,14,50]
s = Solution()
print(s.mincostTickets(days, costs))
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        if n < m:
            return self.maxUncrossedLines(nums2, nums1)

        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                curr = dp[j]
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j-1], curr)
                prev = curr

        return dp[m]


nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
s = Solution()
print(s.maxUncrossedLines(nums1, nums2))
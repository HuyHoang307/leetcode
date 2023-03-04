from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        start, leftBound, iMax, iMin, res = -1, -1, -1, -1, 0

        for i, num in enumerate(nums):
            if num > maxK or num < minK:
                start = i
            if num == minK:
                iMin = i
                leftBound = min(iMax, iMin)
            if num == maxK:
                iMax = i
                leftBound = min(iMax, iMin)
            if leftBound - start > 0:
                res += (leftBound - start)
        return res   

nums = [1,3,5,2,7,5]
minK = 1
maxK = 5

s = Solution()
print(s.countSubarrays(nums, minK, maxK))
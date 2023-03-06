from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) >> 1
            count = arr[mid] - mid - 1
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left + k


arr = [2,3,4,7,11]
k = 5
s = Solution()
print(s.findKthPositive(arr, k))
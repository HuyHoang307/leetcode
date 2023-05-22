from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        s = sorted(s.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in s[:k]]


nums = [1,1,1,2,2,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
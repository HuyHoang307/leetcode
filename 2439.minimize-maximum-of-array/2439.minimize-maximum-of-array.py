from math import ceil
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_ave = 0
        sum_num = 0 
        for i in range(len(nums)):
            sum_num+=nums[i]
            if sum_num/(i+1) > max_ave:
                max_ave = ceil(sum_num/(i+1))
        return max_ave


nums = [3,7,1,6]
s = Solution()
print(s.minimizeArrayValue(nums))

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod

nums = [2, 3, 4 ,5, 6, 7]
target = 9
s = Solution()
print(s.numSubseq(nums, target))

# nums = [2 3 4 5 6 7]
# ind  = [0 1 2 3 4 5]
# l = 0 r = 5 => 2 ^ 4 + 2 ^ 3 + 2 ^ 2 + 2 ^ 1 + 2 ^ 0 + 1 = 2 ^ 5
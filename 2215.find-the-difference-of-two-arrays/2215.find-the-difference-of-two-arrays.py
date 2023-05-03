from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1-s2), list(s2-s1)]
    

nums1 = [52, -21]
nums2 = [22, 66, 89, 52, -56, 5, 22, -70, 99]
s = Solution()
print(s.findDifference(nums1, nums2))




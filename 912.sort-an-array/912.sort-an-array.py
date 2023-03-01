from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nMin = min(nums)
        nMax = max(nums)
        return self.quickSort(nums, nMin, nMax)

# QuickSort
    def quickSort(self, nums: List[int], nMin: int, nMax: int) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        pivot = (nMin + nMax) >> 1
        nums1 = []
        nums2 = []
        nums3 = []
        for num in nums:
            if num == pivot:
                nums3.append(num)
            elif num > pivot:
                nums2.append(num)
            else:
                nums1.append(num)
        return self.quickSort(nums1, nMin, pivot - 1) + nums3 + self.quickSort(nums2, pivot + 1, nMax)
    
# MergeSort
    def mergeSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        mid = n >> 1
        left = self.mergeSort(nums[: mid ])
        right = self.mergeSort(nums[ mid :])
        return self.merge(left, right, mid, n - mid)
    
    def merge(self, left: List[int], right: List[int], llen: int, rlen: int):
        res = []
        i = 0
        j = 0
        while i < llen and j < rlen:
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i == llen:
            return res + right[j:]
        return res + left[i:]




nums = [5,1,1,2,0, 0]
s = Solution()
print(s.sortArray(nums))

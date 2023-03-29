from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total = 0
        cur_sum = 0
        for val in satisfaction:
            cur_sum += val
            if (cur_sum < 0):
                break
            total += cur_sum
        return total
                
            
    
satisfaction = [0,-8,-1,5,-9]
s = Solution()
print(s.maxSatisfaction(satisfaction))
        
from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(totalTime: int) -> bool:
            total = sum(totalTime // t for t in time)
            return total >= totalTrips
        
        low, high = min(time), max(time) * totalTrips
        while high > low:
            mid = (low + high) >> 1
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low

    
time = [5,10,10]
totalTrips = 9
s = Solution()
print(s.minimumTime(time, totalTrips))
        
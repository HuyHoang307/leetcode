
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, count=0, len(people)-1, 0
        while i<=j :
            if people[i] + people[j] <= limit:
                i+=1
            j-=1
            count+=1
        return count

    
people = [5,1,4,2]
limit = 6
s = Solution()
print(s.numRescueBoats(people, limit))

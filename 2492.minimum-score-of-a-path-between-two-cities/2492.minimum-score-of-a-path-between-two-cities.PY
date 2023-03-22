from collections import defaultdict, deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        visited = [False] * (n + 1)
        edges = defaultdict(list)
        for c1 , c2, d in roads:
            edges[c1].append((c2, d))
            edges[c2].append((c1, d))
        res = float('inf')

        queue = deque([1])
        visited[1] = True
        while queue:
            city = queue.popleft()
            for nextCity, dis in edges[city]:
                res = min(res, dis)
                if not visited[nextCity]:
                    queue.append(nextCity)
                    visited[nextCity] = True
        
        return res
            

            


n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
s = Solution()
print(s.minScore(n, roads))
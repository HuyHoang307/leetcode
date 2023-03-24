from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in connections:
            graph[u].append([v, 1]) # forward edge
            graph[v].append([u, 0]) # backward edge

        q = deque([0])
        seen = {0}
        ans = 0

        while q:
            city = q.popleft()
            for nextCity, cost in graph[city]:
                if nextCity not in seen:
                    seen.add(nextCity)
                    ans += cost 
                    q.append(nextCity)
        return ans

    
n = 3
connections = [[1,0],[2,0]]
s = Solution()
print(s.minReorder(n, connections))
                
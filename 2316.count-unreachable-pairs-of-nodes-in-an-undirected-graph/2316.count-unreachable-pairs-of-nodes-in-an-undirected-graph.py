from collections import defaultdict, deque
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        side = defaultdict(list)
        for n1, n2 in edges:
            side[n1].append(n2)
            side[n2].append(n1)
        
        visited = [False] * n
        res, factor = 0, 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                stack = deque([i])
                count = 1
                while stack:
                    node = stack.pop()
                    for nextNode in side[node]:
                        if not visited[nextNode]:
                            count += 1
                            visited[nextNode] = True
                            stack.append(nextNode)
                res += factor * count
                factor += count
        return res
    
n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
s = Solution()
print(s.countPairs(n, edges))
                    
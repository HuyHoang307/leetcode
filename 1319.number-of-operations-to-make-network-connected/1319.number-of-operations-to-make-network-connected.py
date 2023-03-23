from collections import defaultdict, deque
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n -1:
            return -1
        
        connected = [False] * n
        edges = defaultdict(list)
        for c1, c2 in connections:
            edges[c1].append(c2)
            edges[c2].append(c1)
        
        res = 0
        for i in range(n):
            if not connected[i]:
                res += 1
                stack = deque([i])
                connected[i] = True
                while stack:
                    computer = stack.pop()
                    for c in edges[computer]:
                        if not connected[c]:
                            stack.append(c)
                            connected[c] = True
        return res
    
n = 4
connections = [[0,1],[0,2],[1,2]]
s = Solution()
print(s.makeConnected(n, connections))
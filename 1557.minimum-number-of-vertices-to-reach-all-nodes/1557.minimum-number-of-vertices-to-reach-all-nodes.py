from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        should_include = [True] * n
        for e in edges:
            should_include[e[1]] = False
        return [i for i in range(n) if should_include[i]]

n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
s = Solution()
print(s.findSmallestSetOfVertices(n, edges))

from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [0] * len(edges)
        order, ans = 1, -1
        for node, visit in enumerate(visited):
            if visit:
                continue
            start_visited = order
            while node >= 0:
                if visited[node]:
                    if visited[node] >= start_visited:
                        ans = max(ans, order - visited[node])
                    break
                visited[node] = order
                order += 1
                node = edges[node]
        return ans
    
edges = [3,3,4,2,3]
s = Solution()
print(s.longestCycle(edges))
                


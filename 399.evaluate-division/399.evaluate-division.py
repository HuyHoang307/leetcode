from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(x, y, graph, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for neighbor in graph[x]:
                if neighbor not in visited:
                    quotient = graph[x][neighbor]
                    sub_quotient = dfs(neighbor, y, graph, visited)
                    if sub_quotient > 0:
                        return quotient * sub_quotient
            return -1.0
        graph = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        results = []
        for x, y in queries:
            if x not in graph or y not in graph:
                results.append(-1.0)
            elif x == y:
                results.append(1.0)
            else:
                visited = set()
                results.append(dfs(x, y, graph, visited))
        return results

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
s = Solution()
print(s.calcEquation(equations, values, queries))

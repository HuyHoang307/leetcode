from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
      colors = [-1 for i in range(len(graph))]

      def dfs(node, color):
        if colors[node] == color:
          return True
        if colors[node] == (color+1) % 2:
          return False

        colors[node] = color
        children = graph[node]
        for child in children:
          if not dfs(child, (color+1) % 2):
            return False
        return True

      for i in range(len(graph)):
        if colors[i] == -1:
          if not dfs(i, 0):
            return False

      return True








graph = [[1], [0, 3], [3], [1, 2]]
s = Solution()
print(s.isBipartite(graph))

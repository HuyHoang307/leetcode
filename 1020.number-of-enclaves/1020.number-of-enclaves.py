from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        for i in [0, m-1]:
            for j in range(n):
                dfs(i, j)
        for i in range(m):
            for j in [0, n-1]:
                dfs(i, j)
        return sum(sum(i) for i in grid)
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
s = Solution()
print(s.numEnclaves(grid))

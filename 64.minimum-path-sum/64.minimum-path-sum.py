from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(1, m):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for i in range(1, n):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[n-1][m-1]
    
grid = [[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]]
s = Solution()
print(s.minPathSum(grid))


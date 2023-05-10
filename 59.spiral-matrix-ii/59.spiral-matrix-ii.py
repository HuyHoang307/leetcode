from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        start = 1
        res[i][j] = start
        start += 1
        while start <= n * n:
            while j + 1 < n and res[i][j + 1] == 0:
                j += 1
                res[i][j] = start
                start += 1
            while i + 1 < n and res[i + 1][j] == 0:
                i += 1
                res[i][j] = start
                start += 1
            while j - 1 >= 0 and res[i][j - 1] == 0:
                j -= 1
                res[i][j] = start
                start += 1
            while i - 1 >= 0 and res[i - 1][j] == 0:
                i -= 1
                res[i][j] = start
                start += 1
        return res

    
n = 3
s = Solution()
print(s.generateMatrix(n))


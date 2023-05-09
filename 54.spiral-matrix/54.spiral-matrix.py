from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        while i < m-1 and j < n - 1:
            res += matrix[i][j:n]
            for k in range(i + 1, m - 1):
                res.append(matrix[k][n-1])
            tmp = matrix[m-1][j:n]
            tmp.reverse()
            res += tmp
            for k in range(m-2, i, -1):
                res.append(matrix[k][j])
            i += 1
            j += 1
            m -= 1
            n -= 1
        if i == m - 1:
            res += matrix[i][j:n]
        elif j == n - 1:
            for k in range(i, m):
                res.append(matrix[k][n-1])
        return res


matrix = [[1, 11], [2, 12], [3, 13], [4, 14], [5, 15],
          [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]]
s = Solution()
print(s.spiralOrder(matrix))




from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        if (n == 1):
            return mat[0][0]
        m = n+1
        for i in range(n):
            if (n > 1):

                sum += mat[i][i]

                sum += mat[i][n-1-i]

        if (n % 2 == 1):
            sum -= mat[n//2][n//2]

        return sum
    

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.diagonalSum(sum))            


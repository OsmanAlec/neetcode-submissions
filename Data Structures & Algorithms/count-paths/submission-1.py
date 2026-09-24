class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                unique[i][j] = unique[i-1][j] + unique[i][j-1]
        
        return unique[m-1][n-1]
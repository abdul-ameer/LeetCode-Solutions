class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.dp = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dp[i][j] = self.dfs(matrix, m, n, i, j)
        maxPath = 0
        for i in range(m):
            maxPath = max(maxPath, max(self.dp[i]))
        return maxPath
    
    def dfs(self, matrix: List[List[int]], m: int, n: int, r: int, c: int) -> int:
        if 0 <= r < m and 0 <= c < n:
            if self.dp[r][c] is None:
                north = east = south = west = 0
                if 0 <= (r - 1) < m and matrix[r][c] < matrix[r - 1][c]:
                    north = self.dfs(matrix, m, n, r - 1, c)
                if 0 <= (r + 1) < m and matrix[r][c] < matrix[r + 1][c]:
                    south = self.dfs(matrix, m, n, r + 1, c)
                if 0 <= (c - 1) < n and matrix[r][c] < matrix[r][c - 1]:
                    west = self.dfs(matrix, m, n, r, c - 1)
                if 0 <= (c + 1) < n and matrix[r][c] < matrix[r][c + 1]:
                    east = self.dfs(matrix, m, n, r, c + 1)
                self.dp[r][c] = 1 + max(north, east, south, west)
            return self.dp[r][c]
        return 0
        
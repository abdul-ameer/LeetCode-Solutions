class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        for solution in self.queens(n, 0, [], [], []):
            board = ["".join('Q' if i == j  else '.' for i in range(len(solution))) for j in solution]      
            res.append(board)
        return res

    def queens(self, n, i, a, b, c):
        if i < n:
            for j in range(n):
                if j not in a and i+j not in b and i-j not in c:
                    yield from self.queens(n, i+1, a+[j], b+[i+j], c+[i-j])
        else:
            yield a
        
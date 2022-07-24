class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for num in matrix:
            if target in num:
                return True
        return False
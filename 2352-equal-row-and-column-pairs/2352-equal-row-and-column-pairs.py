class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        num_of_pairs = 0
        col_count = Counter(zip(*grid))
        for row in grid:
            num_of_pairs += col_count[tuple(row)]
        
        return num_of_pairs
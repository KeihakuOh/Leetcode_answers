from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import Counter
        patterns = []
        for row in matrix:
            patterns.append(tuple(row))
        
        count = Counter(patterns)
        max_rows = 0
        for pattern in count:
            complement = tuple(1 - x for x in pattern)
            total = count[pattern] + count[complement]
            if total > max_rows:
                max_rows = total
                
        return max_rows

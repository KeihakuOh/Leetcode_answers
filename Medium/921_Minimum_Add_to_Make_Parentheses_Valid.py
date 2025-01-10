class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0 
        moves = 0
        for char in s:
            if char == '(':
                open_count += 1  
            elif char == ')':
                if open_count > 0:
                    open_count -= 1  
                else:
                    moves += 1 
        moves += open_count
        return moves
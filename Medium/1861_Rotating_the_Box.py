class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            empty = len(row) - 1 
            
            for i in range(len(row) - 1, -1, -1):  
                if row[i] == "#":  
                    if i != empty: 
                        row[i], row[empty] = ".", "#"  
                    empty -= 1 
                elif row[i] == "*":  
                    empty = i - 1  

        return [list(row) for row in zip(*box[::-1])]
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for opoperation in operations:
            if "++" in opoperation:
                X += 1
            else:
                X -= 1
        return X

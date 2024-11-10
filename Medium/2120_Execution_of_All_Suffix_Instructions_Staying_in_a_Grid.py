class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            count = 0
            current = startPos[:]
            for j in s[i:]:
                if j == "R" and current[1] < n - 1:
                    current[1] += 1
                    count += 1
                elif j == "D" and current[0] < n - 1:
                    current[0] += 1
                    count += 1
                elif j == "L" and current[1] > 0:
                    current[1] -= 1
                    count += 1
                elif j == "U" and current[0] > 0:
                    current[0] -= 1
                    count += 1
                else:
                    break
                    
            ans.append(count)
        return ans

            
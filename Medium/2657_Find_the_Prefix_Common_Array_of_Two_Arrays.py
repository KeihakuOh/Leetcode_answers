class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            count = 0
            sub_A = A[:i + 1]
            sub_B = B[:i + 1]
            for j in sub_A:
                if j in sub_B:
                    count += 1
            ans.append(count)
        return ans
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [0] * n
        sortedDeck = sorted(deck)
        q = deque([i for i in range(n)])
        j = 0
        while q:
            index = q.popleft()
            ans[index] = sortedDeck[j]
            j += 1
            if q:
                ele = q.popleft()
                q.append(ele)
        return ans
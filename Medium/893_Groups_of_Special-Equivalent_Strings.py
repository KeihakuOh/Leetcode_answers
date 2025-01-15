class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        unique_signatures = set()
        for word in words:
            unique_signatures.add(self.signature(word))

        return len(unique_signatures)

    def signature(self, word):
        even_chars = sorted(word[0::2])
        odd_chars = sorted(word[1::2])
        return tuple(even_chars + odd_chars)
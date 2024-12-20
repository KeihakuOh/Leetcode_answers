class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(word: str) -> List[int]:
            return [word.index(char) for char in word]
        pattern_encoding = encode(pattern)  
        result = []
        for word in words:
            if encode(word) == pattern_encoding:
                result.append(word)
        return result
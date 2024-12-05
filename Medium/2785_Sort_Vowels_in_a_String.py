from collections import deque

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        vowel_chars = []
        
        for char in s:
            if char in vowels:
                vowel_chars.append(char)
        
        vowel_chars.sort()
    
        ans = list(s)
        vowel_index = 0  
        for i, char in enumerate(s):
            if char in vowels:
                ans[i] = vowel_chars[vowel_index]
                vowel_index += 1
        
        return "".join(ans)

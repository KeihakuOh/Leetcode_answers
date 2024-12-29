class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16} 
        state = 0 
        state_map = {0: -1}  
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                state ^= vowels[char]
            if state in state_map:
                max_length = max(max_length, i - state_map[state])
            else:
                state_map[state] = i
        return max_length
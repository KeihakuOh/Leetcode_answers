class Solution:
    # Class variable to store vowels. Using a class variable ensures that all instances of this class share the same vowels set.
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    def reverseVowels(self, s: str) -> str:
        left_index, right_index = 0, len(s) - 1
        characters = list(s)

        while left_index < right_index:
            while not self.isVowel(s[left_index]) and left_index < right_index:
                left_index += 1
            while not self.isVowel(s[right_index]) and left_index < right_index:
                right_index -= 1

            # Swap the characters at the pointers only if both are vowels.
            # This ensures no unnecessary swaps occur if there are no vowels in the string.
            if self.isVowel(characters[left_index]) and self.isVowel(characters[right_index]):
                self.swapVowels(characters, left_index, right_index) 

            left_index += 1
            right_index -= 1

        return "".join(characters)

    def isVowel(self, character: str) -> bool:
        return character in Solution.vowels

    def swapVowels(self, characters: list, left_index: int, right_index: int) -> None:
        characters[left_index], characters[right_index] = characters[right_index], characters[left_index]
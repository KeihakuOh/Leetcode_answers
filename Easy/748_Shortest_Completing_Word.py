from collections import Counter
from typing import List
import unittest

class Solution:
    def shortest_completing_word(self, license_plate: str, words: List[str]) -> str:
        """
        Find the shortest completing word from a given list of words that contains all
        the letters in the given license_plate (ignoring digits and spaces and treating
        letters case-insensitively).
        A completing word must have at least as many occurrences of each character as
        it appears in license_plate.

        Args:
            license_plate (str): A string that may contain letters, digits, and spaces.
            words (List[str]): A list of candidate words.

        Returns:
            str: The shortest completing word from the list.
                If multiple words match the required frequency and have the same length,
                the first one in the list is returned.

        Example:
            >>> solution = Solution()
            >>> solution.shortest_completing_word("1s3 PSt", ["step", "steps", "stripe", "stepple"])
            'steps'
        """
        license_letter_counts = self.count_license_letters(license_plate)
        min_length = float('inf')
        shortest_word = ""

        for word in words:
            if self.is_completing_word(word, license_letter_counts):
                if len(word) < min_length:
                    min_length = len(word)
                    shortest_word = word

        return shortest_word

    def count_license_letters(self, license_plate: str) -> Counter:
        """
        Extract the frequency of letters from the given license_plate, ignoring digits
        and spaces. Converts all letters to lowercase.

        Args:
            license_plate (str): A string containing letters, digits, and spaces.

        Returns:
            Counter: A dictionary-like object containing letter frequencies.
        
        Example:
            >>> solution = Solution()
            >>> solution.count_license_letters("1s3 PSt")
            Counter({'s': 2, 'p': 1, 't': 1})
        """
        letters = [char.lower() for char in license_plate if char.isalpha()]
        return Counter(letters)

    def is_completing_word(self, word: str, license_letter_counts: Counter) -> bool:
        """
        Check if a word is a completing word by ensuring it contains all the required
        letters from the license plate in the necessary frequency.

        Args:
            word (str): The word to check.
            license_letter_counts (Counter): The letter counts from the license plate.

        Returns:
            bool: True if the word is a completing word, otherwise False.

        Example:
            >>> solution = Solution()
            >>> solution.is_completing_word("steps", Counter({'s': 2, 'p': 1, 't': 1}))
            True
        """
        word_letter_counts = Counter(word.lower())
        return all(word_letter_counts[letter] >= license_letter_counts[letter] for letter in license_letter_counts)
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_shortest_completing_word(self):
        self.assertEqual(self.solution.shortest_completing_word("1s3 PSt", ["step", "steps", "stripe", "stepple"]), "steps")
        self.assertEqual(self.solution.shortest_completing_word("aBc 123", ["abc", "bac", "cab"]), "abc")
        self.assertEqual(self.solution.shortest_completing_word("1s3 456", ["looks","pest","stew","show"]), "pest")

if __name__ == "__main__":
    unittest.main()

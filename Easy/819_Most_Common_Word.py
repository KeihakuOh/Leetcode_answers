import pytest
from collections import Counter
import re
from typing import List

class Solution:
    def most_common_word(self, paragraph: str, banned_words: List[str]) -> str:
        """
        Returns the most frequent word in the given paragraph, excluding banned words.

        Args:
            paragraph (str): The input paragraph containing words.
            banned_words (List[str]): A list of words that should be excluded.

        Returns:
            str: The most frequently occurring word in lowercase.
        """
        words = self.extract_words(paragraph)
        valid_word_frequencies = self.count_valid_words(words, banned_words)
        return self.get_most_frequent_valid_word(valid_word_frequencies)

    def extract_words(self, text: str) -> List[str]:
        """
        Extracts words from a given text and converts them to lowercase.

        Args:
            text (str): The input text.

        Returns:
            List[str]: A list of words in lowercase.
        """
        return [word.lower() for word in re.findall(r'\w+', text)]

    def count_valid_words(self, words: List[str], banned_words: List[str]) -> Counter:
        """
        Counts the occurrences of words that are not in the banned words list.

        Args:
            words (List[str]): A list of words extracted from the text.
            banned_words (List[str]): A list of words that should be excluded.

        Returns:
            Counter: A dictionary-like object mapping words to their occurrence counts.
        """
        banned_set = set(banned_words)
        return Counter(word for word in words if word not in banned_set)

    def get_most_frequent_valid_word(self, valid_word_frequencies: Counter) -> str:
        """
        Retrieves the most frequently occurring word.

        Args:
            valid_word_frequencies (Counter): A Counter object with valid word occurrence counts.

        Returns:
            str: The most frequently occurring word.
        """
        return valid_word_frequencies.most_common(1)[0][0]

# ---------------------------- TEST CASES ----------------------------

@pytest.fixture
def solution():
    """Fixture to create a Solution instance for each test."""
    return Solution()

def test_most_common_word(solution):
    """
    Test three cases:
    1. Basic example with banned words.
    2. Single word with punctuation.
    3. Case insensitivity and punctuation handling.
    """
    # Example 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    assert solution.most_common_word(paragraph1, banned1) == "ball"

    # Example 2
    paragraph2 = "a."
    banned2 = []
    assert solution.most_common_word(paragraph2, banned2) == "a"

    # Example 3
    paragraph3 = "Hello hello HELLO world!"
    banned3 = ["world"]
    assert solution.most_common_word(paragraph3, banned3) == "hello"

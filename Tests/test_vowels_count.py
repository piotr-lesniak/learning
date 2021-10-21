import unittest

from Text.VowelsCount import vowels_count


class VowelsCountTestCases(unittest.TestCase):
    def test_vowels_count_in_unit_string(self):
        self.assertEqual(vowels_count('House'), 3)

    def test_vowels_count_in_unit_string_without_vowel(self):
        self.assertEqual(vowels_count('MGM'), 0)

    def test_total_vowels_count_in_multiple_strings(self):
        self.assertEqual(vowels_count("Hi, It's Piter."), 4)
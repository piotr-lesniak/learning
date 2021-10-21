import unittest

from Text.WordsCount import words_count


class WordsCountTestCases(unittest.TestCase):
    def test_words_count_for_one_word(self):
        self.assertEqual(words_count('asd'), 1)

    def test_words_count_for_two_words(self):
        self.assertEqual(words_count('asd rr'), 2)

    def test_words_count_for_many_words(self):
        self.assertEqual(words_count('asd. rr tt oo-r'), 4)
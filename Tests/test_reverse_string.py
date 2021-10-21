import unittest

from Text.ReverseString import reverse_string


class ReverseStringTestCases(unittest.TestCase):
    def test_string(self):
        self.assertEqual(reverse_string('asdfgh'), 'hgfdsa')

    def test_empty(self):
        self.assertEqual(reverse_string(''), '')

    def test_space(self):
        self.assertEqual(reverse_string(' '), ' ')

    def test_spaces(self):
        self.assertEqual(reverse_string('      '), '      ')

    def test_char_with_multispaces(self):
        self.assertEqual(reverse_string(' 2     '), '     2 ')
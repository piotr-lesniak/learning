import unittest

from Text.CheckIfPalindrome import check_if_palindrome


class CheckIfPalindromeTestCases(unittest.TestCase):
    def test_check_that_string_is_palindrome(self):
        self.assertEqual(check_if_palindrome('asdsa'), True)

    def test_check_that_string_is_not_palindrome(self):
        self.assertEqual(check_if_palindrome('asds'), False)
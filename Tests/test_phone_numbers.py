import unittest

from Regex.PhoneNumbers import check_phone_number_is_valid


class PhoneNumbersTestCases(unittest.TestCase):
    def test_phone_number_is_valid(self):
        self.assertTrue(check_phone_number_is_valid('123-222-789'))

    def test_phone_number_is_not_valid(self):
        self.assertFalse(check_phone_number_is_valid('123-222-7899'))
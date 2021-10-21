import unittest

from Regex.PostalCode import validate_postal_code

#postal_codes = [('12-123', True), ('00-000', True), ('1-1', False)]


class PostalCodesTestCases(unittest.TestCase):
    def test_postal_code(self):
        self.assertEqual(validate_postal_code('22-111'), True)

    def test_wrong_postal_code(self):
        self.assertFalse(validate_postal_code('2-111'), False)

    def test_empty_postal_code(self):
        self.assertFalse(validate_postal_code(''), False)

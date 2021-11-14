import unittest

from Numbers.CanBeDivided import can_divide


class CheckIfCanBeDivided(unittest.TestCase):
    def test_check_that_can_be_divided(self):
        self.assertTrue(can_divide(2, 8, 14))

    def test_check_that_can_not_be_divided(self):
        self.assertFalse(can_divide(3, 6, 8))
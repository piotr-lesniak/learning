import unittest

from Text.Maskify import maskify

param_list = [
    ('1234-3322-0000-4597', '####-####-####-4597'),
    ('0000-0000-0000-0000', '####-####-####-0000'),
    ('0000-4597', '####-4597'),
    ('1234-3322-0000-9999', '####-####-####-9999')
]


class CheckMaskify(unittest.TestCase):
    def test_maskify(self):
        for p1, p2 in param_list:
            with self.subTest(msg='Checking maskify(s)', s=p1):
                self.assertEqual(maskify(p1), p2)
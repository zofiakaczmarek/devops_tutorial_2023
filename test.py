import unittest
from example import ArithmeticPair as AP

class TestArithmetic(unittest.TestCase):
    def test_sum(self):
        ap = AP(15, 3)
        ret = ap.sum()
        self.assertEqual(ret, 18, f"error in sum")

    def test_difference(self):
        ap = AP(15, 3)
        ret = ap.difference()
        self.assertEqual(ret, 12, f"error in difference")

    def test_product(self):
        ap = AP(15, 3)
        ret = ap.product()
        self.assertEqual(ret, 45, f"error in product")

    def test_quotient(self):
        ap = AP(15, 3)
        ret = ap.quotient()
        self.assertEqual(ret, 5.0, f"error in quotient")

if __name__ == "__main__":
    unittest.main()

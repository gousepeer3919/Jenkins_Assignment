import unittest
from checkleap import CheckLeap
class TestCheckLeap(unittest.TestCase):
    def test_cl1(self):
        result = CheckLeap(2020)
        self.assertEqual(result,"leap Year")
    def test_cl2(self):
        result = CheckLeap(2024)
        self.assertEqual(result,"leap Year")
    def test_cl3(self):
        result = CheckLeap(2026)
        self.assertEqual(result,"leap Year")
    def test_cl4(self):
        result = CheckLeap(2028)
        self.assertEqual(result,"leap Year")
    def test_cl5(self):
        result = CheckLeap(2027)
        self.assertEqual(result,"leap Year")

if __name__ == '__main__':
    unittest.main()

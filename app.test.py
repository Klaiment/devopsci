import unittest

from app import multiplication, division, addition, puissance, soustraction


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(3,5), 15)

    def test_division(self):
        self.assertEqual(division(6,3), 2)

    def test_addition(self):
        self.assertEqual(addition(3,5), 8)

    def test_soustraction(self):
        self.assertEqual(soustraction(3,2), 1)

    def test_soustraction_with_failed(self):
        self.assertEqual(soustraction(3,2), 5)

    def test_puissance(self):
        self.assertEqual(puissance(2,3), 8)


if __name__ == '__main__':
    unittest.main()

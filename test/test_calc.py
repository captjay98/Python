import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):

        self.assertEqual(calc.add(5, 8), 13)
        self.assertEqual(calc.add(-5, 5), 0)
        self.assertEqual(calc.add(-5, -5), -10)

    def test_sub(self):
        self.assertEqual(calc.sub(10,2), 8)
        self.assertEqual(calc.sub(-10,2), -12)
        self.assertEqual(calc.sub(-2,-2), 0)

    def test_mul(self):
        self.assertEqual(calc.mul(5,5), 25)
        self.assertEqual(calc.mul(-2,2), -4)
        self.assertEqual(calc.mul(-2,-2), 4)

    def test_div(self):
        self.assertEqual(calc.div(-10,2), -5)
        self.assertEqual(calc.div(10,2), 5)
        self.assertEqual(calc.div(2,2), 1)
        
        self.assertRaises(ValueError, calc.div, 0, 0)
        with self.assertRaises(ValueError):
            calc.divide(0,0)

if __name__ == '__main__':
    unittest.main()
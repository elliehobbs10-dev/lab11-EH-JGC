# https://github.com/elliehobbs10-dev/lab11-EH-JGC.git
# Partner 1: Ellie Hobbs
# Partner 2: Jose Garcia-Cejas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(4, -10), -6)
        self.assertNotEqual(add(5, 5),6)

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, -5), 15)
        self.assertNotEqual(subtract(3, 2), 5)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(4, 10), 2.5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    def test_logarithm(self):
        self.assertEqual(logarithm(10, 1), 0)
        self.assertEqual(logarithm(5, 25), 2)
        self.assertNotEqual(logarithm(8, 2), 5)

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
              logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2), 1.41421356)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

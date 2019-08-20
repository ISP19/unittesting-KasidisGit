import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class."""

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertNotEqual(Fraction(3, 5), Fraction(1, 12).__add__(Fraction(2, 3)))
        with self.assertRaises(ValueError):
            Fraction(1, 0).__add__(Fraction(1, 0))
        with self.assertRaises(TypeError):
            Fraction("a", "b").__add__(Fraction("a"))
        with self.assertRaises(TypeError):
            Fraction(1, "b").__add__(Fraction("a", 0))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(Fraction(1, 0) == Fraction(2000, 0))
        self.assertTrue(Fraction(-1, 0).__eq__(Fraction(-2000, 0)))
        self.assertFalse(Fraction(0, 0) == Fraction(2000, 0))

    def test_sub(self):
        self.assertEqual(Fraction(1), Fraction(3, 2) - Fraction(1, 2))
        self.assertNotEqual(Fraction(3), Fraction(3, 2).__sub__(Fraction(1, 2)))
        with self.assertRaises(ValueError):
            Fraction(1, 0).__sub__(Fraction(1, 0))
        with self.assertRaises(TypeError):
            Fraction("a", "b").__sub__(Fraction("a"))
        with self.assertRaises(TypeError):
            Fraction(1, "b").__sub__(Fraction("a", 0))

    def test_gt(self):
        self.assertTrue(Fraction(2), Fraction(1, 2))
        self.assertFalse(Fraction(0).__gt__(Fraction(1, 2)))
        self.assertTrue(Fraction(1, 0).__gt__(Fraction(-1, 0)))
        self.assertFalse(Fraction(-1, 0).__gt__(Fraction(-1, 0)))
        self.assertFalse(Fraction(1, 0).__gt__(Fraction(2000, 0)))

    def test_ng(self):
        self.assertTrue(Fraction(-1, 2), Fraction(1, 2))
        self.assertFalse(Fraction(4, 2).__neg__() > 0)
        with self.assertRaises(ValueError):
            Fraction(1, 0).__neg__()
        with self.assertRaises(TypeError):
            Fraction("a", "b").__neg__()
        with self.assertRaises(TypeError):
            Fraction(1, "b").__neg__()

    def test_mul(self):
        self.assertEqual(Fraction(1, 4), Fraction(1, 2) * Fraction(1, 2))
        self.assertNotEqual(Fraction(1, 4), Fraction(1, 2) * Fraction(1, 3))
        with self.assertRaises(ValueError):
            Fraction(1, 0).__mul__(Fraction(1, 0))
        with self.assertRaises(TypeError):
            Fraction("a", "b").__mul__(Fraction("a"))
        with self.assertRaises(TypeError):
            Fraction(1, "b").__mul__(Fraction("a", 0))

    def test_div(self):
        self.assertTrue(Fraction(1), (Fraction(1, 2) / Fraction(1, 2)))
        self.assertTrue(Fraction(1), (Fraction(1, 2).__truediv__(Fraction(1, 2))))
        with self.assertRaises(ValueError):
            Fraction(1, 0).__truediv__(Fraction(1, 0))
        with self.assertRaises(TypeError):
            Fraction("a", "b").__truediv__(Fraction("a"))
        with self.assertRaises(TypeError):
            Fraction(1, "b").__truediv__(Fraction("a", 0))

    def check_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

        # TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0

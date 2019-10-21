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
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(1500, 1500)
        self.assertEqual("1",f.__str__())


    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertNotEqual(Fraction(3, 5), Fraction(1, 12).__add__(Fraction(2, 3)))
        with self.assertRaises(TypeError):
            Fraction("a", "b").__add__(Fraction("a"))


    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertEqual(False,((Fraction(0,0).__str__).__eq__(Fraction(0,0).__str__)))

    def test_sub(self):
        self.assertEqual(Fraction(1), Fraction(3, 2) - Fraction(1, 2))
        self.assertNotEqual(Fraction(3), Fraction(3, 2).__sub__(Fraction(1, 2)))
        with self.assertRaises(TypeError):
            Fraction(1, "b").__sub__(Fraction("a", 0))
        self.assertEqual("Indeterminate Form", Fraction(1, 0) - Fraction(1, 0))
        self.assertEqual("Determinate Form", Fraction(1, 0) - Fraction(-1, 0))
        self.assertEqual(Fraction(1), Fraction(3, 2).__sub__(Fraction(1, 2)))
        

    def test_gt(self):
        self.assertTrue(Fraction(2), Fraction(1, 2))
        self.assertFalse(Fraction(0).__gt__(Fraction(1, 2)))
        self.assertTrue(Fraction(1, 0).__gt__(Fraction(-1, 0)))
        self.assertFalse(Fraction(-1, 0).__gt__(Fraction(-1, 0)))



    def test_ng(self):
        self.assertTrue(Fraction(-1, 2), Fraction(1, 2))
        self.assertFalse(Fraction(4, 2).__neg__() > 0)
        with self.assertRaises(TypeError):
            Fraction("a", "b").__neg__()
        with self.assertRaises(ValueError):
            Fraction(0, 0).__neg__()

    def test_mul(self):
        self.assertEqual(Fraction(1, 4), Fraction(1, 2) * Fraction(1, 2))
        with self.assertRaises(TypeError):
            Fraction(1, "b").__mul__(Fraction("a", 0))
        self.assertEqual(Fraction(-1, 6), Fraction(-1, 2).__mul__(Fraction(1, 3)))


        



    def test_div(self):
        self.assertTrue(Fraction(1), (Fraction(1, 2) / Fraction(1, 2)))
        self.assertTrue(Fraction(1), (Fraction(1, 2).__truediv__(Fraction(1, 2))))
        with self.assertRaises(TypeError):
            Fraction(1, "b").__truediv__(Fraction("a", 0))

    def test_determinate_form(self):


        self.assertTrue("Determinate Form", Fraction(-1, 0) / Fraction(-1, 0))
        self.assertTrue("Determinate Form", Fraction(1, 0) - Fraction(1, 0))
        self.assertTrue("Determinate Form", Fraction(0) * Fraction(1, 0))

    def test_gcd(self):
        self.assertEqual(30,Fraction.gcd(self,30,90))

if __name__ == '__main__':
     unittest.main(verbosity=2)
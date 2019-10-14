import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.
    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        self.numerator = numerator
        self.denominator = denominator
        if denominator is not 0:
            self.fraction = self.numerator / self.denominator

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        try:
            if self.denominator is not 0 and frac.denominator is not 0:
                new_numerator = self.numerator * frac.denominator + self.denominator * frac.numerator  # compute numerator of self + frac
                new_denominator = self.denominator * frac.denominator  # compute denominator of self + frac
                return Fraction(new_numerator, new_denominator)
        except TypeError:
            raise ValueError("Input must be integer")
        else:
            return "Determinate Form"

    # TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    # Optional have fun and overload other operators such as
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)
    def __sub__(self, frac):
        try:
            if self.denominator is not 0 and frac.denominator is not 0:
                new_numerator = self.numerator * frac.denominator - self.denominator * frac.numerator
                new_denominator = self.denominator * frac.denominator
                return Fraction(new_numerator, new_denominator)
        except TypeError:
            raise ValueError("Input must be integer")
        else:
            if self.numerator > 0 and frac.numerator > 0:
                return "Indeterminate Form"
            return "Determinate Form"

    def __mul__(self, frac):
        try:
            if self.denominator is not 0 and frac.denominator is not 0:
                new_numerator = self.numerator * frac.numerator
                new_denominator = self.denominator * frac.denominator
                return Fraction(new_numerator, new_denominator)
        except TypeError:
            raise ValueError("Input must be integer")
        else:
            if self.numerator is 0 or frac.numerator is 0:
                return "Indeterminate Form"
            return "Determinate Form"

    def __truediv__(self, frac):
        try:
            if self.denominator is not 0 and frac.denominator is not 0:
                new_numerator = self.numerator * frac.denominator
                new_denominator = self.denominator * frac.numerator
                return Fraction(new_numerator, new_denominator)
        except TypeError:
            raise ValueError("Input must be integer")
        else:
            return "Indeterminate Form"

    def __gt__(self, frac):
        if frac.denominator is 0 and self.denominator is 0:
            return self.numerator > frac.numerator
        if self.denominator is 0:
            self.numerator = frac.numerator + 1
            self.denominator = 1
        elif frac.denominator is 0:
            frac.numerator = self.numerator + 1
            frac.denominator = 1
        return self.numerator > frac.numerator

    def __neg__(self):
        try:
            if self.denominator is not 0:
                return -self.fraction
        except TypeError:
            raise ValueError("Input must be integer")
        else:
            raise ValueError("Undefined")

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        if self.denominator is 0 and frac.denominator is 0:
            if self.numerator >= 0 and frac.numerator <= 0:
                self.fraction = 1
                frac.fraction = -1
            elif self.numerator <= 0 and frac.numerator >= 0:
                self.fraction = -1
                frac.fraction = 1
            else:
                self.fraction = 0
                frac.fraction = 0
        return self.fraction == frac.fraction

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        if self.denominator is 0:
            return "Indeterminate Form"
        if self.numerator % self.denominator == 0:
            return f"{self.fraction:.0f}"
        else:
            return f"{(self.numerator/(self.gcd(self.numerator,self.denominator))):.0f}/{((self.denominator/self.gcd(self.numerator,self.denominator))):.0f}"

print(Fraction(1,0))

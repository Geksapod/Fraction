"""This module provides access to class Fraction."""
import math

class Fraction:
    """
    Convert two integer numbers to a fraction.

    Args:
        num(int): The numerator of the fraction.
        denom (int): The denominator of the fraction.
    """

    def __init__(self, num: int, denom: int):
        if not isinstance(num, int):
            raise TypeError("Numerator must be integer")
        if not isinstance(denom, int):
            raise TypeError("Denominator must be integer")
        if not denom:
            raise ZeroDivisionError("Denominator can not be zero")

        self.__num = num
        self.__denom = denom

    def dec_fract(self):
        """
        Return decimal value of the fractional.
        If numerator is equal to zero the function return 0.
        """

        if self.__denom and not self.__num:
            return 0
        elif self.__denom:
            return self.__num / self.__denom

    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.dec_fract() > other.dec_fract()

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.dec_fract() < other.dec_fract()

    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.dec_fract() >= other.dec_fract()

    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.dec_fract() <= other.dec_fract()

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.dec_fract() == other.dec_fract()

    def __add__(self, other):
        """Return self+other."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__num * other.__denom + (other.__num * self.__denom)), (self.__denom * other.__denom))

    def __radd__(self, other):
        """Return other+self."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__num * other.__denom + (other.__num * self.__denom)), (self.__denom * other.__denom))

    def __sub__(self, other):
        """Return self-other."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__num * other.__denom - (other.__num * self.__denom)), (self.__denom * other.__denom))

    def __rsub__(self, other):
        """Return other-self."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__num * other.__denom - (other.__num * self.__denom)), (self.__denom * other.__denom))

    def __mul__(self, other):
        """Return self*other."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__num * other.__num), (self.__denom * other.__denom))

    def __rmul__(self, other):
        """Return other*self."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__num * other.__num), (self.__denom * other.__denom))

    def __truediv__(self, other):
        """Return self/other."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__num * other.__denom), (self.__denom * other.__num))

    def __rtruediv__(self, other):
        """Return other/self."""

        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction((self.__denom * other.__num), (self.__num * other.__denom))

    def sign_fract(self):
        """
        If fraction is positive number returns 1.
        If fraction is negative number returns -1.
        """

        sign = 1 if self.__num * self.__denom > 0 else -1
        return sign

    def __str__(self):
        num_abs = abs(self.__num)
        denom_abs = abs(self.__denom)
        gcd_fract = math.gcd(self.__num, self.__denom)
        simp_num = num_abs // gcd_fract
        simp_denom = denom_abs // gcd_fract

        if not self.__num:
            return "0"
        if simp_denom == 1:
            return f"{self.sign_fract() * simp_num}"
        if simp_num > simp_denom:
            int_part = simp_num // simp_denom
            simp_num = simp_num - int_part * simp_denom
            return f"{self.sign_fract() * int_part} {simp_num}/{simp_denom}"
        return f"{self.sign_fract() * simp_num}/{simp_denom}"


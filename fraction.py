"""This module provides access to class Fraction"""
import math

class Fraction:
    """Convert two integer numbers to a fraction"""



    def __init__(self, num1: int, num2: int):

        self.num1 = num1
        self.num2 = num2


    def __str__(self):
        if self.num1 > self.num2 and (math.gcd(self.num1, self.num2) !=0 or math.gcd(self.num1, self.num2) !=1):
            pass

            return f"{self.num1 // self.num2} {self.num1 % self.num2}/{self.num2}"

        else:
            return f"{self.num1}/{self.num2}"


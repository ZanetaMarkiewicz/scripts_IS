from unittest import TestCase
from D14_script import Calculator


class CalculatorTest(TestCase):

    def test_multiply_values(self):
        multiply_result = Calculator.multiply(2, 3)
        self.assertEqual(6, multiply_result, "2 multiply 6 should be 6")

    def test_power_values(self):
        power_result = Calculator.power(2, 2)
        self.assertEqual(4, power_result, "2 to the power of 2 is 4")

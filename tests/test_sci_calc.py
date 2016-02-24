import unittest

from projects import sci_calc


class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.calc = sci_calc.Arithmetic()

    def test_addition(self):
        result = self.calc.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtraction(self):
        result = self.calc.subtract(3, 4)
        self.assertEqual(result, -1)

    def test_multiply(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_exponents(self):
        result = self.calc.to_power(3, 4)
        self.assertEqual(result, 81)


class TestTrigonometry(unittest.TestCase):
    def test_logarithmic_operations(self):
        pass

    def test_trigonometry(self):
        pass


class TestAltMaths(unittest.TestCase):
    def test_hexadecimal(self):
        pass

    def test_octal(self):
        pass

    def test_Boolean_math(self):
        pass

    def test_complex_numbers(self):
        pass

    def test_scientific_notation(self):
        pass

    def test_fractions(self):
        pass


class TestStats(unittest.TestCase):
    def test_statistics(self):
        pass

    def test_probability(self):
        pass


    def test_matrix_calculations(self):
        pass

    def test_calculus(self):
        pass

    def test_physical_constants(self):
        pass

class TestUnitConversion(unittest.TestCase):
    def test_unit_conversion(self):
        pass

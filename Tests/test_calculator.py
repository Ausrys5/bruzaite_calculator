import unittest

from ..calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add_method_adds_correctly_to_memory(self):
        # Create an instance of the Calculator class
        calculator = Calculator()

        # Add a value to the calculator's memory
        result = calculator.add(5)

        # Assert that the calculator's memory has been updated correctly
        self.assertEqual(result, 5)

        # Add another value to the calculator's memory
        result = calculator.add(7.5)

        # Assert that the calculator's memory has been updated correctly
        self.assertEqual(result, 12.5)

        # Add a non-numeric value to the calculator's memory
        result = calculator.add('abc')

        # Assert that the calculator's memory remains unchanged
        self.assertEqual(result, 12.5)

        # Add None to the calculator's memory
        result = calculator.add(None)

        # Assert that the calculator's memory remains unchanged
        self.assertEqual(result, 12.5)


def test_subtract_method_subtracts_correctly_from_memory(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Subtract a value from the calculator's memory
    result = calculator.subtract(5)

    # Assert that the calculator's memory has been updated correctly
    self.assertEqual(result, -5)

    # Subtract another value from the calculator's memory
    result = calculator.subtract(7.5)

    # Assert that the calculator's memory has been updated correctly
    self.assertEqual(result, -12.5)

    # Subtract a non-numeric value from the calculator's memory
    result = calculator.subtract('abc')

    # Assert that the calculator's memory remains unchanged
    self.assertEqual(result, -12.5)

    # Subtract None from the calculator's memory
    result = calculator.subtract(None)

    # Assert that the calculator's memory remains unchanged
    self.assertEqual(result, -12.5)


def test_multiply_method_multiplies_correctly_to_memory(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Add a value to the calculator's memory
    result = calculator.multiply(5)

    # Assert that the calculator's memory has been updated correctly
    self.assertEqual(result, 0)

    # Multiply the calculator's memory with another value
    result = calculator.multiply(3.5)

    # Assert that the calculator's memory has been updated correctly
    self.assertEqual(result, 0)

    # Multiply the calculator's memory with a non-numeric value
    result = calculator.multiply('abc')

    # Assert that the calculator's memory remains unchanged
    self.assertEqual(result, 0)

    # Multiply the calculator's memory with None
    result = calculator.multiply(None)

    # Assert that the calculator's memory remains unchanged
    self.assertEqual(result, 0)


def test_divide_method_divides_correctly_to_memory(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Add a value to the calculator's memory
    calculator.add(10)

    # Divide the calculator's memory with a value
    result = calculator.divide(2)

    # Assert that the calculator's memory has been updated correctly
    self.assertEqual(result, 5)

    # Divide the calculator's memory with a non-numeric value
    result = calculator.divide('abc')

    # Assert that the calculator's memory remains unchanged
    self.assertEqual(result, 5)

    # Divide the calculator's memory with None
    result = calculator.divide(None)

    # Assert that the calculator's memory remains unchanged
    self.assertEqual(result, 5)

    # Divide the calculator's memory with zero
    result = calculator.divide(0)

    # Assert that the calculator's memory remains unchanged
    self.assertEqual(result, 5)


def test_nth_root_positive_integer(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Set the calculator's memory to 27
    calculator.memory = 27

    # Calculate the cube root of the calculator's memory
    result = calculator.nth_root(3)

    # Assert that the result is 3
    self.assertEqual(result, 3)


def test_nth_root_negative_integer_even_root(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Set the calculator's memory to -8
    calculator.memory = -8

    # Attempt to calculate the 4th root of the calculator's memory
    result = calculator.nth_root(4)

    # Assert that a ValueError is raised
    self.assertRaises(ValueError)


def test_nth_root_negative_integer_odd_root(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Set the calculator's memory to -27
    calculator.memory = -27

    # Calculate the cube root of the calculator's memory
    result = calculator.nth_root(3)

    # Assert that the result is -3
    self.assertEqual(result, -3)


def test_nth_root_non_number(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Attempt to calculate the square root of a string
    result = calculator.nth_root('abc')

    # Assert that a TypeError is raised
    self.assertRaises(TypeError)


def test_reset_method_sets_memory_to_zero(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Add a value to the calculator's memory
    calculator.add(5)

    # Reset the calculator's memory
    result = calculator.reset()

    # Assert that the calculator's memory has been set to zero
    self.assertEqual(result, 0)


def test_init_method_initializes_memory_to_zero(self):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Assert that the calculator's memory has been initialized to zero
    self.assertEqual(calculator.memory, 0)


if __name__ == '__main__':
    unittest.main()

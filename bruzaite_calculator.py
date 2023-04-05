from typing import Union

class BruzaiteCalculator:
    # This class represents a simple calculator with a memory that
    # can perform basic arithmetic operations.

    def __init__(self):
        # Initializes the calculator's memory to 0.
        self.memory = 0

    def add(self, x: Union[int, float]) -> Union[int, float]:
        '''
        Adds the value x to the calculator's memory.

        Args:
            x (int or float): The value to add to the calculator's memory.

        Returns:
            The updated value of the calculator's memory after the addition.
        '''
        try:
            if not isinstance(x, (int, float)):
                raise TypeError("Input must be a number")
            self.memory += x
            return self.memory
        except TypeError as type_error:  # Handle TypeError
            print(type_error)
            return self.memory
        except ValueError as value_error:  # Handle ValueError
            print(value_error)
            return self.memory

    def subtract(self, x: Union[int, float]) -> Union[int, float]:
        '''
        Subract the value x from the calculator's memory.

        Args:
            x (int or float): The value to subtract from
            the calculator's memory.

        Returns:
            The updated value of the calculator's memory after the subtraction.
        '''
        try:
            if not isinstance(x, (int, float)):
                raise TypeError("Input must be a number")
            self.memory -= x
            return self.memory
        except TypeError as type_error:  # Handle TypeError
            print(type_error)
            return self.memory
        except ValueError as value_error:  # Handle ValueError
            print(value_error)
            return self.memory

    def multiply(self, x: Union[int, float]) -> Union[int, float]:
        '''
        Multiply the calculator's memory by the value x.

        Args:
            x (int, float, or str): The value to multiply
            the calculator's memory by.
            If the value is a string, it will be converted
            to int or float before multiplying.
            If x is None or not a number, a TypeError will be raised.

        Returns:
            The updated value of the calculator's memory
            after the multiplication.
        '''
        try:
            if isinstance(x, str):
                x = int(x) if x.isdigit() else float(x)
            if x is None or not isinstance(x, (int, float)):
                raise TypeError("Input must be a number")
            self.memory *= x
            return self.memory
        except TypeError as type_error:  # Handle TypeError
            print(type_error)
            return self.memory
        except ValueError as value_error:  # Handle ValueError
            print(value_error)
            return self.memory

    def divide(self, x: Union[int, float]) -> Union[int, float]:
        '''
        Divide the calculator's memory by the number x.

        Args:
            x (int, float, or str): The value to divide the calculator's
            memory by. If the value is a string,
            It will be converted to int or float before dividing.
            If x is None or not a number, a TypeError will be raised.

        Returns:
            The updated value of the calculator's memory after the division.
        '''
        try:
            if x is None or not isinstance(x, (int, float)):
                raise TypeError("Input must be a number")
            self.memory /= x
            return self.memory
        except ZeroDivisionError as zero_division_error:
            print(zero_division_error)
            return self.memory
        except TypeError as type_error:  # Handle TypeError
            print(type_error)
            return self.memory
        except ValueError as value_error:  # Handle ValueError
            print(value_error)
            return self.memory

    def nth_root(self, n: Union[int, float]) -> Union[int, float, str, None]:
        try:
            if not isinstance(n, (int, float)):
                raise TypeError("n must be a number")
            if n <= 0:
                raise ValueError("n must be a positive number")
            if not isinstance(self.memory, (int, float)):
                raise TypeError("Memory must be a number")
            if self.memory < 0 and n % 2 == 0:
                raise ValueError("Cannot take even root of a negative number!")
            if self.memory < 0 and n % 2 != 0:
                self.memory = -((-self.memory) ** (1/n))
            else:
                self.memory **= (1/n)
            return self.memory
        except OverflowError as over_flow_error:
            print(over_flow_error)
            return "Result is too large to be represented"
            
    def reset(self) -> None:
        '''
        Resets the calculator's memory to 0.
        '''
        self.memory = 0
        return self.memory
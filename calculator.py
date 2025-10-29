def add(a, b)
    result = a + b
    # Missing return statement

def divide(x, y):
    return x / y  # No zero division check

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # No check for empty list

import math
import os  # unused import

def get_square_root(n):
    if n < 0:
        return "Error"  # Should raise exception
    return math.sqrt(n)

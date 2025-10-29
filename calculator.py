
def add(a, b):
    return a + b

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError('Cannot calculate average of empty list')
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

import math

def get_square_root(n):
    if n < 0:
        raise ValueError('Cannot calculate square root of negative number')
    return math.sqrt(n)

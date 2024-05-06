#!/usr/bin/python3
import sys

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: ./your_script.py <number>")
    sys.exit(1)

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError as e:
    print(e)


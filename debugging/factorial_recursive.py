#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given integer.

# Parameters:
# - n: An integer for which the factorial will be calculated.

# Returns:
# The factorial of the input integer n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the factorial of the integer provided as a command-line argument.
f = factorial(int(sys.argv[1]))

# Print the calculated factorial.
print(f)


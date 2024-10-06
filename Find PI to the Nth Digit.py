# Import required libraries and modules
from __future__ import print_function  # Ensures compatibility between Python 2 and 3
import math
import sys
from decimal import Decimal, getcontext, ROUND_FLOOR  # Import ROUND_FLOOR

# Set rounding behavior and recursion limit
getcontext().rounding = ROUND_FLOOR  # Corrected ROUND_FLOOR import
sys.setrecursionlimit(100000)  # Increases the recursion limit for large calculations


# Recursive function to calculate factorial of a number
def recursive_factorial(number):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    number -- Number for which the factorial will be calculated.
    """
    if not number:
        return 1
    return number * recursive_factorial(number - 1)


# Function to compute the iterated value based on the Chudnovsky Algorithm
def calculate_iterations(decimal_digits):
    """
    Compute the iterated sum in the Chudnovsky Algorithm for Pi calculation.

    Parameters:
    decimal_digits -- The number of decimal digits required for Pi calculation.
    """
    decimal_digits += 1  # To ensure the precision includes the desired decimal digits
    getcontext().prec = decimal_digits  # Set precision for Decimal calculations

    iteration_sum = 0  # Initialize sum
    for current_iteration in range(decimal_digits):
        # Apply Chudnovsky formula components
        numerator = recursive_factorial(6 * current_iteration) * (13591409 + 545140134 * current_iteration)
        denominator = recursive_factorial(3 * current_iteration) * (recursive_factorial(current_iteration)) ** 3 * (
                    640320 ** (3 * current_iteration))
        iteration_sum += numerator / denominator  # Sum each iteration

    return Decimal(iteration_sum)


# Function to compute the value of Pi
def calculate_pi(decimal_digits):
    """
    Calculate the value of Pi using the Chudnovsky Algorithm.

    Parameters:
    decimal_digits -- The number of decimal places required.
    """
    iterations_result = calculate_iterations(decimal_digits)  # Get the iterated sum
    constant_multiplier = 426880 * math.sqrt(10005)  # Constant from the Chudnovsky Algorithm
    pi_value = Decimal(constant_multiplier) / iterations_result  # Final Pi value

    return pi_value


# Shell function to interact with users via the console
def interactive_shell():
    """
    Interactive shell that allows users to input the number of decimal places for Pi calculation.

    No parameters or return values.
    """
    print("Welcome to the Pi Calculator!")
    print("Enter the number of decimal places for Pi calculation, or type 'quit' to exit.")

    while True:
        print(">>> ", end='')
        user_input = input()  # Use input() for Python 3
        if user_input.lower() == "quit":
            break  # Exit the shell when 'quit' is entered
        elif not user_input.isdigit():  # Check if the input is a valid number
            print("Invalid input! Please enter a valid number.")
        else:
            # Calculate and display Pi value for valid input
            print(calculate_pi(int(user_input)))


# Main function to start the shell
if __name__ == '__main__':
    interactive_shell()

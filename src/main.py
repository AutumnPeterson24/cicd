"""
Multiple of 10 number checker
Author: Autumn Peterson
"""


def is_mult_of_10(num: int) -> bool:
    """Return True if num is a multiple of 10, False otherwise."""
    if num == 0:
        return False
    return num % 10 == 0


def is_mult_of_10_str(num: str) -> str:
    """Return a string indicating whether num is a multiple of 10."""
    if num.isnumeric():
        return f"{num} is {'a multiple of 10' if is_mult_of_10(int(num)) else 'not a multiple of 10'}."
    else:
        return "Please enter a number."

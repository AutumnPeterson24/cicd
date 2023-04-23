"""
cube-root number checker
Author: Autumn Peterson
"""


def is_cube_root(num: float) -> bool:
    """Return True if num is a cube-root, False otherwise."""
    if num == 1 or num == -1:
        return True
    if (round(abs(num ** (1/3))) % 3) == 0 or (round(abs(num ** (1/3))) % 2) == 0 or (round(abs(num ** (1/3))) % 5) == 0 or (round(abs(num ** (1/3))) % 7) == 0:
        return True


def is_cube_root_str(num: str) -> str:
    """Return a string indicating whether num is a cube root."""
    if num.lstrip("-").isnumeric():
        return f"(+/-) {num.lstrip('-')} is {'a cube-root' if is_cube_root(float(num)) else 'not a cube-root'}."
    else:
        return "Please enter a number."

"""
cube-root number checker
Author: Autumn Peterson
"""


def is_cube_root(num: int) -> bool:
    """Return True if num is a cube-root, False otherwise."""
    return (num ** (1/3) % 3) == 0


def is_cube_root_str(num: str) -> str:
    """Return a string indicating whether num is a cube root."""
    if num == "1":
        return f"{num} is a cube-root."
    if num.isnumeric():
        return f"{num} is {'a cube-root' if is_cube_root(int(num)) else 'not a cube-root'}."
    else:
        return "Please enter a number."

"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from main import is_cube_root, is_cube_root_str


class Test(TestCase):
    def test_is_cube_root(self):
        assert is_cube_root(0)
        assert is_cube_root(27)
        assert not is_cube_root(2)
        assert is_cube_root(1)

    def test_is_odd_str(self):
        assert is_cube_root_str("0") == "0 is a cube-root."
        assert is_cube_root_str("1") == "1 is a cube-root."
        assert is_cube_root_str("2") == "2 is not a cube-root."
        assert is_cube_root_str("-1") == "Please enter a number."
        assert is_cube_root_str("A") == "Please enter a number."
        assert is_cube_root_str("") == "Please enter a number."

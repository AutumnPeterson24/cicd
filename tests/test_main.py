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
        assert is_cube_root(729)
        assert is_cube_root(-64)
        assert is_cube_root(-125)
        assert is_cube_root(343)

    def test_is_odd_str(self):
        assert is_cube_root_str("0") == "0 is a cube-root."
        assert is_cube_root_str("1") == "1 is a cube-root."
        assert is_cube_root_str("343") == "343 is a cube-root."
        assert is_cube_root_str("-64") == "-64 is a cube-root."
        assert is_cube_root_str("729") == "729 is a cube-root."
        assert is_cube_root_str("-125") == "-125 is a cube-root."
        assert is_cube_root_str("2") == "2 is not a cube-root."
        assert is_cube_root_str("-1") == "-1 is a cube-root."
        assert is_cube_root_str("A") == "Please enter a number."
        assert is_cube_root_str("") == "Please enter a number."

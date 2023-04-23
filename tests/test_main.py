"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from main import is_mult_of_10, is_mult_of_10_str


class Test(TestCase):
    def test_is_mult_of_10(self):
        assert is_mult_of_10(10)
        assert not is_mult_of_10(11)
        assert not is_mult_of_10(227)
        assert is_mult_of_10(1000)
        assert not is_mult_of_10(1)
        assert not is_mult_of_10(0)

    def test_is_mult_of_10_str(self):
        assert is_mult_of_10_str("10") == "10 is a multiple of 10."
        assert is_mult_of_10_str("11") == "11 is not a multiple of 10."
        assert is_mult_of_10_str("a") == "Please enter a number."
        assert is_mult_of_10_str("0") == "0 is not a multiple of 10."


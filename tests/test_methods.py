import pytest
import unittest

check = "Please add some tests!"


class TestSimple(unittest.TestCase):

    def test_some_method(self):
        assert check == "Please add some tests!"


if __name__ == '__main__':
    unittest.main()

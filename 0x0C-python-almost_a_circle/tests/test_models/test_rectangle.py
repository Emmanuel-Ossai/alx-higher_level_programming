#!/usr/bin/python3


"""
This is a unittests for rectangle
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_instantiation(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    # Rest of the test cases follow...

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_area(self):
        r = Rectangle(2, 4)
        self.assertEqual(8, r.area())

    def test_display(self):
        r = Rectangle(2, 3, 0, 0, 0)
        self.assertEqual("##\n##\n##\n", r.display())

    def test_str(self):
        r = Rectangle(4, 6)
        self.assertEqual("[Rectangle] ({}) 0/0 - 4/6\n".format(r.id), str(r))

    # Rest of the test cases follow...


if __name__ == "__main__":
    unittest.main()

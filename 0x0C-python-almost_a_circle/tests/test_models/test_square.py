#!/usr/bin/python3
"""This is a  unittests for square
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """test of Square class."""

    def test_instantiation(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.id, s2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

    def test_size_validation(self):
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)

    def test_x_validation(self):
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_y_validation(self):
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_to_dictionary(self):
        s = Square(5, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'x': 2, 'size': 5, 'y': 1})

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1, size=8)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 8)

if __name__ == "__main__":
    unittest.main()

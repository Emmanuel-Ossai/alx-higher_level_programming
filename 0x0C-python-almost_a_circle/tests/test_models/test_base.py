#!/usr/bin/python3
"""
This is a unittests for base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """This is a Unittests for testing instantiation."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    # Add the rest of the test methods for Base instantiation...


class TestBaseToJsonString(unittest.TestCase):
    """This is a Unittests for testing to_json_string."""

    def test_to_json_string_rectangle_type(self):
        # Test cases for Rectangle.to_json_string()...

    def test_to_json_string_square_type(self):
        # Test cases for Square.to_json_string()...

    # Add the rest of the test methods for Base to_json_string...


class TestBaseSaveToFile(unittest.TestCase):
    """This is a Unittests for testing save_to_file method"""

    def test_save_to_file_one_rectangle(self):
        # Test cases for Rectangle.save_to_file()...

    def test_save_to_file_two_rectangles(self):
        # Test cases for Rectangle.save_to_file()...

    def test_save_to_file_one_square(self):
        # Test cases for Square.save_to_file()...

    # Add the rest of the test methods for Base save_to_file...


class TestBaseFromJsonString(unittest.TestCase):
    """This is a Unittests for testing from_json_string method"""

    def test_from_json_string_type(self):
        # Test cases for Rectangle.from_json_string()...

    def test_from_json_string_one_rectangle(self):
        # Test cases for Rectangle.from_json_string()...

    def test_from_json_string_two_rectangles(self):
        # Test cases for Rectangle.from_json_string()...

    # Add the rest of the test methods for Base from_json_string...


class TestBaseCreate(unittest.TestCase):
    """This is a Unittests for testing create method"""

    def test_create_rectangle_original(self):
        # Test cases for Rectangle.create()...

    def test_create_rectangle_new(self):
        # Test cases for Rectangle.create()...

    def test_create_rectangle_is(self):
        # Test cases for Rectangle.create()...

    # Add the rest of the test methods for Base create...


class TestBaseLoadFromFile(unittest.TestCase):
    """This is a Unittests for testing load_from_file method"""

    def test_load_from_file_first_rectangle(self):
        # Test cases for Rectangle.load_from_file()...

    def test_load_from_file_second_rectangle(self):
        # Test cases for Rectangle.load_from_file()...

    def test_load_from_file_rectangle_types(self):
        # Test cases for Rectangle.load_from_file()...

    # Add the rest of the test methods for Base load_from_file...


class TestBaseSaveToFileCSV(unittest.TestCase):
    """This is a Unittests for testing save_to_file_csv method"""

    def test_save_to_file_csv_one_rectangle(self):
        # Test cases for Rectangle.save_to_file_csv()...

    def test_save_to_file_csv_two_rectangles(self):
        # Test cases for Rectangle.save_to_file_csv()...

    def test_save_to_file_csv_one_square(self):
        # Test cases for Square.save_to_file_csv()...

    # Add the rest of the test methods for Base save_to_file_csv...


class TestBaseLoadFromFileCSV(unittest.TestCase):
    """This is a Unittests for testing load_from_file_csv"""

    def test_load_from_file_csv_first_rectangle(self):
        # Test cases for Rectangle.load_from_file_csv()...

    def test_load_from_file_csv_second_rectangle(self):
        # Test cases for Rectangle.load_from_file_csv()...

    def test_load_from_file_csv_rectangle_types(self):
        # Test cases for Rectangle.load_from_file_csv()...

    # Add the rest of the test methods for Base load_from_file_csv...


if __name__ == "__main__":
    unittest.main()

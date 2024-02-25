#!/usr/bin/python3
"""Test case for the base module"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_class_Base(unittest.TestCase):
    """Test for the class Base"""
    def test_id_is_None(self):
        """test for check if id is none"""
        cls_B = Base(None)
        self.assertEqual(1, cls_B.id)

    def test_id_int(self):
        """id is a number"""
        cls_B = Base(10)
        self.assertEqual(10, cls_B.id)

    def test_id_negative(self):
        """id is a negative number"""
        cls_B = Base(-10)
        self.assertEqual(-10, cls_B.id)

    def test_id_zero(self):
        """id is zero"""
        cls_B = Base(0)
        self.assertEqual(0, cls_B.id)

    def test_id_string(self):
        """id is a string"""
        cls_B = Base("string")
        self.assertEqual("string", cls_B.id)

    def test_id_character(self):
        """id is a character"""
        cls_B = Base("a")
        self.assertEqual("a", cls_B.id)

    def test_id_float(self):
        """id is a float number"""
        cls_B = Base(5.2)
        self.assertEqual(5.2, cls_B.id)

    def test_id_list(self):
        """id is a list"""
        cls_B = Base([1, 2])
        self.assertEqual([1, 2], cls_B.id)

    def test_id_matrix(self):
        """id is a matrix"""
        cls_B = Base([[1, 2], [3, 4]])
        self.assertEqual([[1, 2], [3, 4]], cls_B.id)

    def test_id_tuple(self):
        """id is a tuple"""
        cls_B = Base((1, 2))
        self.assertEqual((1, 2), cls_B.id)

    def test_id_dictionary(self):
        """id is integer"""
        cls_B = Base({"id": 10})
        self.assertEqual({"id": 10}, cls_B.id)

    """----------------JSON FILE----------------"""

    def test_json_string(self):
        """JSON is a string"""
        cls_R = Rectangle(5, 2)
        json_dictionary = cls_R.to_dictionary()
        json_string = Base.to_json_string([json_dictionary])
        self.assertEqual(type(json_string), str)

    def test_json_dictionary(self):
        """Testing the json string"""
        cls_S = Square(16, 4, 4, 3)
        json_dictionary = cls_S.to_dictionary()
        json_dict_list = Base.to_json_string([json_dictionary])
        self.assertEqual(
            json.loads(json_dict_list), [{"size": 16, "x": 4, "y": 4, "id": 3}]
        )

    def test_json_None(self):
        """JSON file is None"""
        cls_R = Rectangle(5, 2, 5, 2, 10)
        json_dictionary = cls_R.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_json_Empty(self):
        """JSON file is empty"""
        cls_R = Rectangle(5, 2, 5, 2, 10)
        json_dictionary = cls_R.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_json_string_None(self):
        """JSON string is None"""
        json_string = None
        None_list = Base.from_json_string(json_string)
        self.assertEqual(None_list, [])

    def test_json_empty_list(self):
        """JSON list is empty"""
        json_string = "[]"
        empty_list = Base.from_json_string(json_string)
        self.assertEqual(empty_list, [])

    def test_json_id_string(self):
        """JSON is dictionary"""
        json_string = '[{ "id": 89 }]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 89}])


if __name__ == "__main__":
    unittest.main()

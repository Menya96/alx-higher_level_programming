#!/usr/bin/python3
"""Class Base unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


mybase = Base()
mybase2 = Base()
mybase3 = Base()
mybase4 = Base(12)
mybase5 = Base()


class TestBaseClass(unittest.TestCase):
    """Test cases for class Base"""
    def test_object_type(self):
        """Checkk type of Base object"""
        self.assertTrue(type(mybase) == Base)

    def test_class_instance(self):
        """Check if Base is an instance of Object"""
        self.assertTrue(isinstance(Base, object))

    def test_class_subclass(self):
        """Check if Base is a subclass of Object"""
        self.assertTrue(issubclass(Base, object))

    def test_id_none(self):
        """Check id not given result"""
        self.assertEqual(mybase.id, 1)

    def test_id_none2(self):
        """Check id not given result"""
        self.assertEqual(mybase2.id, 2)

    def test_id_none3(self):
        """Check id not given result"""
        self.assertEqual(mybase3.id, 3)

    def test_id_given(self):
        """Check id given result"""
        self.assertEqual(mybase4.id, 12)

    def test_id_none5(self):
        """Check id not given result"""
        self.assertEqual(mybase5.id, 4)

    def test_id_zero(self):
        """Check zero id given result"""
        self.assertEqual(Base(0).id, 0)

    def test_id_negative(self):
        """Check negative id given result"""
        self.assertEqual(Base(-8).id, -8)

    def test_id_string(self):
        """Check string id given result"""
        self.assertEqual(Base("hey").id, "hey")

    def test_id_list(self):
        """Check list id given result"""
        self.assertEqual(Base([33, 7, 87]).id, [33, 7, 87])

    def test_id_tuple(self):
        """Check tuple id given result"""
        self.assertEqual(Base((33, 7, 87)).id, (33, 7, 87))

    def test_id_dict(self):
        """Check dictionary id given result"""
        self.assertEqual(Base({"ky": 3, "vlue": 73}).id, {"ky": 3, "vlue": 73})

    def test_type_to_json(self):
        """Checking the type of result to_json_string"""
        rec11 = Rectangle(3, 5)
        rec11JSON = Base.to_json_string([rec11.to_dictionary()])
        self.assertTrue(type(rec11JSON) == str)

    def test_docstring(self):
        """Check if docstring is available"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_got_to_json_string(self):
        """Check if Base has to_json_string method"""
        self.assertTrue("to_json_string" in dir(Base))

    def test_list_none(self):
        """Check None list passed to from_json_string"""
        self.assertEqual(mybase2.to_json_string(None), "[]")

    def test_list_empty(self):
        """Check empty list passed to to_json_string"""
        self.assertEqual(mybase2.to_json_string([]), "[]")

    def test_got_save_to_file(self):
        """Check if Base has save_to_file method"""
        self.assertTrue("save_to_file" in dir(Base))

    def test_got_from_json_string(self):
        """Check if Base has from_json_string method"""
        self.assertTrue("from_json_string" in dir(Base))

    def test_py_list_none(self):
        """Check None list passed to from_json_string"""
        self.assertEqual(mybase3.from_json_string(None), [])

    def test_py_list_empty(self):
        """Check empty list passed to from_json_string"""
        self.assertEqual(mybase3.from_json_string("[]"), [])

    def test_got_create(self):
        """Check if Base has create method"""
        self.assertTrue("create" in dir(Base))

    def test_got_load_from_file(self):
        """Check if Base has load_from_file method"""
        self.assertTrue("load_from_file" in dir(Base))


if __name__ == "__main__":
    unittest.main()

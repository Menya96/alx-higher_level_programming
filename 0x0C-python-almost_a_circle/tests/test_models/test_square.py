#!/usr/bin/python3
"""Class Square unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
from contextlib import redirect_stdout
import io
import sys
from io import StringIO


s1 = Square(5)
s2 = Square(2, 2)
s3 = Square(3, 1, 3, 12)


class TestClassSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_object_type(self):
        """Testing if obje is of type Square"""
        self.assertTrue(type(s1) == Square)

    def test_class_instance_rec(self):
        """If square object is a Square instance"""
        self.assertTrue(isinstance(s1, Square))

    def test_class_instance_base(self):
        """Check if object is an instance of Base"""
        self.assertTrue(isinstance(s1, Base))

    def test_class_instance_obj(self):
        """Check if object is an instance of Object"""
        self.assertTrue(isinstance(s1, object))

    def test_class_subclass(self):
        """Check if a subclass of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_class_subclass(self):
        """Check if a subclass of object"""
        self.assertTrue(issubclass(Square, object))

    def test_class_subclass_base(self):
        """Check if a subclass of Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_sq_area(self):
        """Check square.area() calcuation"""
        self.assertEqual(s1.area(), 25)

    def test_sq_area2(self):
        """Check square.area() calcuation"""
        self.assertEqual(s2.area(), 4)

    def test_sq_area3(self):
        """Check square.area() calcuation"""
        self.assertEqual(s3.area(), 9)

    def test_got_area(self):
        """Check if rectangle has area method"""
        self.assertTrue("area" in dir(s1))

    def test_got_display(self):
        """Check if rectangle has display method"""
        self.assertTrue("display" in dir(s1))

    def test_got_str(self):
        """Check if rectangle has __str__ method"""
        self.assertTrue("__str__" in dir(s1))

    def test_got_update(self):
        """Check if rectangle has update method"""
        self.assertTrue("update" in dir(s1))

    def test_list_arg(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Square([])

    def test_tuple_arg(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Square(())

    def test_none_arg(self):
        """Expects type int not None"""
        with self.assertRaises(TypeError):
            Square(None)

    def test_float_arg(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Square(4.6)

    def test_bool_arg(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Square(True)

    def test_no_args(self):
        """Expects a size argument atleast"""
        with self.assertRaises(TypeError):
            Square()

    def test_extra_args(self):
        """More than required arguments passed"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_objects_type(self):
        """Check type of two Square instances"""
        self.assertTrue(type(s1) and type(s2) == Square)

    def test_string_arg(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Square("2")

    def test_negative_arg(self):
        """Expects greater than 0 int not negative int"""
        with self.assertRaises(ValueError):
            Square(-10)

    def test_negative_arg_y(self):
        """Expects greater than 0 int not negative int"""
        with self.assertRaises(ValueError):
            Square(10, 2, -1)

    def test_dict_arg(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Square(10, 2, {})

    def test_id_none3(self):
        """Testing given id value"""
        self.assertEqual(s3.id, 12)

    def test_got_dictionary(self):
        """Check if square has to_dictionary method"""
        self.assertTrue("to_dictionary" in dir(s1))

    def test_got_to_json_string(self):
        """Check if square has to_json_string method"""
        self.assertTrue("to_json_string" in dir(Square))

    def test_list_none(self):
        """Check None list passed to to_json_string"""
        self.assertEqual(s2.to_json_string(None), "[]")

    def test_list_empty(self):
        """Check empty list passed to to_json_string"""
        self.assertEqual(s2.to_json_string([]), "[]")

    def test_got_from_json_string(self):
        """Check if Square has from_json_string method"""
        self.assertTrue("from_json_string" in dir(Square))

    def test_got_save_to_file(self):
        """Check if Square has save_to_file method"""
        self.assertTrue("save_to_file" in dir(Square))

    def test_py_list_none(self):
        """Check None list passed to from_json_string"""
        self.assertEqual(s2.from_json_string(None), [])

    def test_py_list_empty(self):
        """Check empty list passed to from_json_string"""
        self.assertEqual(s2.from_json_string("[]"), [])

    def test_got_create(self):
        """Check if Square has create method"""
        self.assertTrue("create" in dir(Square))

    def test_got_load_from_file(self):
        """Check if Square has load_from_file method"""
        self.assertTrue("load_from_file" in dir(Square))

    def test_del(self):
        """Deleting a Square Instance"""
        self.sqq = Square(4)
        del self.sqq

    def test_size_get(self):
        """Getting the Square's size"""
        self.sq5 = Square(2)
        self.assertEqual(self.sq5.size, 2)

    def test_x(self):
        """Getting the Square's x"""
        self.sq5 = Square(9)
        self.sq5.x = 11
        self.assertEqual(self.sq5.x, 11)

    def test_y(self):
        """Getting the Square's y"""
        self.sq5 = Square(3)
        self.assertEqual(self.sq5.y, 0)

    def test_y_setter(self):
        """Setting the Square's y"""
        self.sq5 = Square(3)
        self.sq5.y = 127
        self.assertEqual(self.sq5.y, 127)

    def test_string_x(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Square(5, "2")

    def test_string_y(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Square(5, 7, "2")

    def test_dict_y(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Square(10, 2, {})

    def test_list_y(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Square(2, 8, [])

    def test_tuple_y(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Square(10, 33, ())

    def test_float_y(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Square(2, 6, 8.9)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Square(10, None)

    def test_bool_y(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Square(10, 2, False)

    def test_negative_arg_y(self):
        """Expects a int greater than 0"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_dict_x(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Square(16, {})

    def test_list_x(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Square(29, [])

    def test_tuple_x(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Square(10, ())

    def test_float_x(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Square(12, 8.9)

    def test_negative_x(self):
        """Expects positive int not negative"""
        with self.assertRaises(ValueError):
            Square(10, -3)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Square(2, None)

    def test_bool_x(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Square(10, False)

    def test_zero_size(self):
        """Expects type int not zero"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Testing the object's string output"""
        sq13 = Square(7, 4, 3, 16)
        answr = "[Square] (16) 4/3 - 7"
        self.assertEqual(sq13.__str__(), answr)

    def test_id_update(self):
        """Checking if update method works"""
        self.sq35 = Square(3)
        self.sq35.update(90)
        self.assertEqual(self.sq35.id, 90)

    def test_size_update(self):
        """Checking if update method works"""
        self.sq17 = Square(3)
        self.sq17.update(90, 4)
        self.assertEqual(self.sq17.size, 4)

    def test_x_update(self):
        """Checking if update method works"""
        self.sq17 = Square(3)
        self.sq17.update(90, 4, 7)
        self.assertEqual(self.sq17.x, 7)

    def test_y_update(self):
        """Checking if update method works"""
        self.sq17 = Square(3)
        self.sq17.update(90, 4, 7, 5)
        self.assertEqual(self.sq17.y, 5)

    def test_kwargs_update(self):
        """Checking if update method works"""
        self.sq17 = Square(2)
        self.sq17.update(x=9, id=8, y=33, size=11)
        self.assertEqual(self.sq17.x, 9)
        self.assertEqual(self.sq17.id, 8)
        self.assertEqual(self.sq17.y, 33)
        self.assertEqual(self.sq17.size, 11)

    def test_kwargs_n_args(self):
        """Checking use of args and kwargs together"""
        self.sq17 = Square(2)
        self.sq17.update(77, x=9, id=8, y=33, size=11)
        self.assertEqual(self.sq17.id, 77)

    def test_to_dict_type(self):
        """Check type returned from to_dictionary"""
        sq88 = Square(47)
        self.assertEqual(type(sq88.to_dictionary()), dict)

    def test_no_size(self):
        """Check error raised if argument is missing"""
        with self.assertRaises(TypeError):
            Square()

    def test_save_to_file_arg(self):
        """Test weird argument that can be passed"""
        with self.assertRaises(TypeError):
            Square.save_to_file(False)

    def test_to_dict_inst(self):
        """Compare to_dictionary instances"""
        sq9 = Square(6, 5)
        sq9Dict = sq9.to_dictionary()
        sq8 = Square.create(**sq9Dict)
        self.assertNotEqual(sq9, sq8)

    def test_nb_objects(self):
        """Test and check order of object creation"""
        s7 = Square(79)
        s99 = Square(14)
        self.assertEqual(s7.id, s99.id - 1)

    def test_private_x(self):
        """Test printing out the private attribute"""
        with self.assertRaises(AttributeError):
            sr7 = Square(7, 9, 5, 4)
            print(sr7.__x)

    def test_private_y(self):
        """Test printing out the private attribute"""
        with self.assertRaises(AttributeError):
            sqr7 = Square(7, 9, 4, 2)
            print(sqr7.__y)

    def test_square_height(self):
        """Check square's height"""
        ss = Square(7)
        self.assertEqual(ss.height, 7)

    def test_square_width(self):
        """Check square's width"""
        ss = Square(7)
        self.assertEqual(ss.width, 7)

    def test_square_x(self):
        """Check square's x"""
        ss = Square(7)
        self.assertEqual(ss.x, 0)

    def test_square_y(self):
        """Check square's y"""
        ss = Square(7)
        self.assertEqual(ss.y, 0)

    def test_bytes_size(self):
        """Pass bytes for size argument"""
        with self.assertRaises(TypeError):
            Square(b'Kotlin')

    def test_range_size(self):
        """Pass range for size argument"""
        with self.assertRaises(TypeError):
            Square(range(9))

    def test_nan_size(self):
        """Pass nan for size argument"""
        with self.assertRaises(TypeError):
            Square(float("nan"))

    def test_to_dict_print(self):
        """Test to_dictionary print"""
        sq2 = Square(5, 90, 5, 37)
        sq2dict = sq2.to_dictionary()
        answ = {'size': 5, 'id': 37, 'x': 90, 'y': 5}
        self.assertEqual(sq2dict, answ)

    def test_none_save_to_file(self):
        """Checking empty list saved if method failed"""
        try:
            os.remove("Square.json")
        except:
            pass
        sqr = Square(5, 0, 0, 346)
        Square.save_to_file(None)
        with open("Square.json", "r") as afile:
            dta = afile.read()
        self.assertEqual("[]", dta)

    def test_empty_save_to_file(self):
        """Checking empty list saved if method failed"""
        try:
            os.remove("Square.json")
        except:
            pass
        sqr = Square(5, 0, 0, 346)
        Square.save_to_file([])
        with open("Square.json", "r") as afile:
            dta = afile.read()
        self.assertEqual("[]", dta)

    def test_save_to_file2(self):
        """Test save to file two"""
        try:
            os.remove("Square.json")
        except:
            pass
        sq1 = Square(5, 0, 0, 87)
        Square.save_to_file([sq1])
        with open("Square.json", "r") as sqFile:
            sqData = sqFile.read()
        self.assertEqual(str, type(sqData))
        try:
            os.remove("Square.json")
        except:
            pass

    def test_load_from_file_sq(self):
        """Test method load from file in the square"""
        sq2 = Square(10)
        inList = [sq2]
        Square.save_to_file(inList)
        outList = Square.load_from_file()
        self.assertNotEqual(id(sq2), id(outList[0]))

    def test_same_load_from_file(self):
        """Load from the same file test"""
        sq3 = Square(10)
        liin = [sq3]
        Square.save_to_file(liin)
        liout = Square.load_from_file()
        self.assertEqual(sq3.size, liout[0].size)

    def test_x_same_load_from_file(self):
        """Load from the same file test"""
        sq3 = Square(10)
        liin = [sq3]
        Square.save_to_file(liin)
        liout = Square.load_from_file()
        self.assertEqual(sq3.x, liout[0].x)

    def test_output_to_dictionary_sq(self):
        """Test to_dictionary method output"""
        sq62 = Square(21, 43, 55, 67)
        sq62dict = sq62.to_dictionary()
        ans = {'size': 21, 'id': 67, 'x': 43, 'y': 55}
        self.assertEqual(sq62dict, ans)

    def test_type_to_dictionary(self):
        """Test to_dictionary dictionary type"""
        sq12 = Square(9)
        self.assertEqual(type(sq12.to_dictionary()), dict)

    def test_display(self):
        """Test for square's display method"""
        sqr = Square(2, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            sqr.display()
            theout = bufferIO.getvalue()
            self.assertEqual(theout, ('#' * 2 + '\n') * 2)
        sqr = Square(2, 3, 4, 5)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            sqr.display()
            theout = bufferIO.getvalue()
            ansr = ('\n' * 4 + (' ' * 3 + '#' * 2 + '\n') * 2)
            self.assertEqual(theout, ansr)

    def test_display_square(self):
        """Testing the square displayed"""
        sqPrinted = StringIO()
        sys.stdout = sqPrinted
        mysq = Square(10)
        mysq.display()
        sys.stdout = sys.__stdout__
        displ = ("##########\n" +
                 "##########\n" +
                 "##########\n" +
                 "##########\n" +
                 "##########\n" +
                 "##########\n" +
                 "##########\n" +
                 "##########\n" +
                 "##########\n" +
                 "##########\n")
        self.assertEqual(sqPrinted.getvalue(), displ)

    def test_no_y_display(self):
        sqr = Square(3, 1)
        listener = TestSquareDisplay.square_stdout(sqr, "display")
        self.assertEqual(" ###\n ###\n ###\n", listener.getvalue())

    def test_no_x_display(self):
        sqx = Square(4, 0, 1, 9)
        lstener = TestSquareDisplay.square_stdout(sqx, "display")
        answ = "\n####\n####\n####\n####\n"
        self.assertEqual(answ, lstener.getvalue())

    def test_all_display(self):
        sqa = Square(2, 3, 2, 1)
        displ = TestSquareDisplay.square_stdout(sqa, "display")
        answ = "\n\n   ##\n   ##\n"
        self.assertEqual(answ, displ.getvalue())

    def test_display_error(self):
        sqe = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sqe.display(90)


class TestSquareDisplay(unittest.TestCase):
    """Class to test square's display method"""

    @staticmethod
    def square_stdout(rec, func):
        """Returns the output printed

        Args:
            rec: a rectangle
            func: any rectangle's method
        """
        displ = io.StringIO()
        sys.stdout = displ
        if func == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return displ


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Class Rectangle unittest"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO
import os
import json
import io


rec = Rectangle(10, 2)
rec2 = Rectangle(2, 10)
rec3 = Rectangle(10, 2, 0, 0, 12)


class TestClassRectangle(unittest.TestCase):
    """Test cases for the Base class"""

    def test_given_id(self):
        """Testing given id value"""
        self.assertEqual(rec3.id, 12)

    def test_object_type(self):
        """Testing if obje is of type Rectangle"""
        self.assertTrue(type(rec) == Rectangle)

    def test_class_instance(self):
        """If Rectangle object is of object class instance"""
        self.assertTrue(isinstance(rec, object))

    def test_class_subclass(self):
        """If Rectangle is a subclass of Base class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_objects_type(self):
        """Comparing two Rectangle instance types"""
        self.assertTrue(type(rec) and type(rec3) == Rectangle)

    def test_string_x(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "2")

    def test_string_y(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 7, "2")

    def test_dict_y(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, {})

    def test_list_y(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 8, [])

    def test_tuple_y(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 33, ())

    def test_float_y(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 6, 8.9)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, None)

    def test_bool_y(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 7, False)

    def test_negative_width(self):
        """Expects a int greater than 0"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_negative_arg_y(self):
        """Expects a int greater than 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_dict_x(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_list_x(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, [])

    def test_tuple_x(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, ())

    def test_float_x(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 8.9)

    def test_negative_x(self):
        """Expects positive int not negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, None)

    def test_bool_x(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, False)

    def test_none_height(self):
        """Expects type int not None"""
        with self.assertRaises(TypeError):
            Rectangle(10, None)

    def test_float_height(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 4.6)

    def test_string_height(self):
        """Expects height int not string"""
        with self.assertRaises(TypeError):
            Rectangle(10, "java")

    def test_list_height(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Rectangle(10, [8, 5])

    def test_negative_height(self):
        """Expects type int not negative int"""
        with self.assertRaises(ValueError):
            Rectangle(10, -9)

    def test_zero_width(self):
        """Expects type int not zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 9)

    def test_zero_height(self):
        """Expects type int not zero"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_dict_height(self):
        """Expects type int not dictionary"""
        with self.assertRaises(TypeError):
            Rectangle(10, {"i": 2, "l": 1})

    def test_tuple_height(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle(10, (7, 5))

    def test_bool_width(self):
        """Expects int width not boolean"""
        with self.assertRaises(TypeError):
            Rectangle(True, 4)

    def test_string_width(self):
        """Expects int width not string"""
        with self.assertRaises(TypeError):
            Rectangle("Bell", 4)

    def test_float_width(self):
        """Expects width int not float"""
        with self.assertRaises(TypeError):
            Rectangle(7.4, 12)

    def test_tuple_width(self):
        """Expects width int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle((1, 3, 4), 4)

    def test_dict_width(self):
        """Expects width int not dict"""
        with self.assertRaises(TypeError):
            Rectangle({"kc": 2, "lp": 9}, 4)

    def test_none_width(self):
        """Expects width int not none"""
        with self.assertRaises(TypeError):
            Rectangle(None, 4)

    def test_no_args(self):
        """Expects a width and a height"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_extra_args(self):
        """Error, pass more than required arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_rec_area(self):
        """Check correct area of the rectangle"""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_rec_area2(self):
        """Check correct area of the rectangle"""
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_rec_area3(self):
        """Correct rectangle area with all args given"""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_got_area(self):
        """Check if rectangle has area method"""
        self.assertTrue("area" in dir(rec))

    def test_got_display(self):
        """Check if rectangle has display method"""
        self.assertTrue("display" in dir(Rectangle(3, 4)))

    def test_got_str(self):
        """Check if rectangle has __str__ method"""
        self.assertTrue("__str__" in dir(rec))

    def test_got_update(self):
        """Check if rectangle has update method"""
        self.assertTrue("update" in dir(rec))

    def test_got_dictionary(self):
        """Check if rectangle has to_dictionary method"""
        self.assertTrue("to_dictionary" in dir(rec))

    def test_got_to_json_string(self):
        """Check if rectangle has to_json_string method"""
        self.assertTrue("to_json_string" in dir(Rectangle))

    def test_got_from_json_string(self):
        """Check if rectangle has from_json_string method"""
        self.assertTrue("from_json_string" in dir(Rectangle))

    def test_py_list_none(self):
        """Check None list passed to from_json_string"""
        self.assertEqual(rec2.from_json_string(None), [])

    def test_py_list_empty(self):
        """Check empty list passed to from_json_string"""
        self.assertEqual(rec2.from_json_string("[]"), [])

    def test_got_create(self):
        """Check if rectangle has create method"""
        self.assertTrue("create" in dir(Rectangle))

    def test_got_load_from_file(self):
        """Check if rectangle has load_from_file method"""
        self.assertTrue("load_from_file" in dir(Rectangle))

    def test_got_save_to_file(self):
        """Check if Rectangle has save_to_file method"""
        self.assertTrue("save_to_file" in dir(Rectangle))

    def test_del(self):
        """Deleting a Rectangle Instance"""
        self.rect = Rectangle(4, 8)
        del self.rect

    def test_width_get(self):
        """Getting the rectangle's width"""
        self.r5 = Rectangle(3, 9)
        self.assertEqual(self.r5.width, 3)

    def test_height_get(self):
        """Getting the rectangle's height"""
        self.r5 = Rectangle(3, 9)
        self.assertEqual(self.r5.height, 9)

    def test_x_getter(self):
        """Getting the rectangle's x"""
        self.r5 = Rectangle(3, 9, 55)
        self.assertEqual(self.r5.x, 55)

    def test_y_getter(self):
        """Getting the rectangle's y"""
        self.r5 = Rectangle(3, 9, 55, 90)
        self.assertEqual(self.r5.y, 90)

    def test_x(self):
        """Getting the rectangle's x"""
        self.r5 = Rectangle(3, 9)
        self.r5.x = 11
        self.assertEqual(self.r5.x, 11)

    def test_y(self):
        """Getting the rectangle's y"""
        self.r5 = Rectangle(3, 9)
        self.assertEqual(self.r5.y, 0)

    def test_str(self):
        """Testing the object's string output"""
        r13 = Rectangle(2, 4, 3, 3, 6)
        answr = "[Rectangle] (6) 3/3 - 2/4"
        self.assertEqual(r13.__str__(), answr)

    def test_id_update(self):
        """Checking if update method works"""
        self.r5 = Rectangle(3, 9)
        self.r5.update(20)
        self.assertEqual(self.r5.id, 20)

    def test_width_update(self):
        """Checking if update method works"""
        self.r5 = Rectangle(3, 9)
        self.r5.update(20, 45)
        self.assertEqual(self.r5.width, 45)

    def test_height_update(self):
        """Checking if update method works"""
        self.r5 = Rectangle(3, 9)
        self.r5.update(20, 45, 3)
        self.assertEqual(self.r5.height, 3)

    def test_x_update(self):
        """Checking if update method works"""
        self.r5 = Rectangle(3, 9)
        self.r5.update(20, 45, 3, 2)
        self.assertEqual(self.r5.x, 2)

    def test_y_update(self):
        """Checking if update method works"""
        self.r5 = Rectangle(3, 9)
        self.r5.update(20, 45, 3, 2, 4)
        self.assertEqual(self.r5.y, 4)

    def test_kwargs_update(self):
        """Checking if update method works"""
        self.r5 = Rectangle(1, 2)
        self.r5.update(x=9, id=8, y=33, height=11)
        self.assertEqual(self.r5.x, 9)
        self.assertEqual(self.r5.id, 8)
        self.assertEqual(self.r5.y, 33)
        self.assertEqual(self.r5.height, 11)

    def test_kwargs_n_args(self):
        """Checking use of args and kwargs together"""
        self.r5 = Rectangle(1, 2)
        self.r5.update(77, x=9, id=8, y=33, height=11)
        self.assertEqual(self.r5.id, 77)

    def test_to_dict_type(self):
        """Check type returned from to_dictionary"""
        r88 = Rectangle(21, 47)
        self.assertEqual(type(r88.to_dictionary()), dict)

    def test_no_height(self):
        """Check error raised if argument is missing"""
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_save_to_file_arg(self):
        """Test weird argument that can be passed"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(False)

    def test_to_dict_inst(self):
        """Compare to_dictionary instances"""
        re4 = Rectangle(6, 8, 5)
        re4Dict = re4.to_dictionary()
        re3 = Rectangle.create(**re4Dict)
        self.assertNotEqual(re4, re3)

    def test_nb_objects(self):
        """Test and check order of object creation"""
        r7 = Rectangle(7, 9)
        r99 = Rectangle(19, 14)
        self.assertEqual(r7.id, r99.id - 1)

    def test_private_width(self):
        """Test printing out the private attribute"""
        with self.assertRaises(AttributeError):
            r7 = Rectangle(7, 9)
            print(r7.__width)

    def test_private_height(self):
        """Test printing out the private attribute"""
        with self.assertRaises(AttributeError):
            r7 = Rectangle(7, 9)
            print(r7.__height)

    def test_private_x(self):
        """Test printing out the private attribute"""
        with self.assertRaises(AttributeError):
            r7 = Rectangle(7, 9, 5, 2)
            print(r7.__x)

    def test_private_y(self):
        """Test printing out the private attribute"""
        with self.assertRaises(AttributeError):
            r7 = Rectangle(7, 9, 4, 2)
            print(r7.__y)

    def test_bytes_width(self):
        """Pass bytes for width argument"""
        with self.assertRaises(TypeError):
            Rectangle(b'Kotlin', 4)

    def test_nan_width(self):
        """Pass nan for width argument"""
        with self.assertRaises(TypeError):
            Rectangle(float("nan"), 10)

    def test_bytes_x(self):
        """Pass bytes for x argument"""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, b'Kotlin')

    def test_bytes_y(self):
        """Pass bytes for y argument"""
        with self.assertRaises(TypeError):
            Rectangle(2, 5, 3, b'Kotlin')

    def test_nan_x(self):
        """Pass nan for x argument"""
        with self.assertRaises(TypeError):
            Rectangle(10, 11, float("nan"))

    def test_nan_y(self):
        """Pass nan for x argument"""
        with self.assertRaises(TypeError):
            Rectangle(10, 11, 42, float("nan"))

    def test_bytes_height(self):
        """Pass bytes for height argument"""
        with self.assertRaises(TypeError):
            Rectangle(4, b'Kotlin')

    def test_nan_height(self):
        """Pass nan for height argument"""
        with self.assertRaises(TypeError):
            Rectangle(10, float("nan"))

    def test_range_height(self):
        """Pass range for height argument"""
        with self.assertRaises(TypeError):
            Rectangle(12, range(9))

    def test_range_x(self):
        """Pass range for x argument"""
        with self.assertRaises(TypeError):
            Rectangle(12, 13, range(9))

    def test_range_y(self):
        """Pass range for y argument"""
        with self.assertRaises(TypeError):
            Rectangle(12, 14, 15, range(9))

    def test_range_width(self):
        """Pass range for width argument"""
        with self.assertRaises(TypeError):
            Rectangle(range(9), 13)

    def test_output_to_dictionary(self):
        """Test to_dictionary method output"""
        r29 = Rectangle(10, 2, 1, 9, 5)
        ans = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(ans, r29.to_dictionary())

    def test_load_from_file_method(self):
        """Test JSON loading from a file"""
        rect1 = Rectangle(10, 7, 2, 8)
        rectLst = [rect1]
        Rectangle.save_to_file(rectLst)
        lstOut = Rectangle.load_from_file()
        self.assertNotEqual(id(rect1), id(lstOut[0]))

    def test_same_y_load_from_file(self):
        """Test JSON loading from a file"""
        rect1 = Rectangle(10, 7, 2, 8)
        rectLst = [rect1]
        Rectangle.save_to_file(rectLst)
        lstOut = Rectangle.load_from_file()
        self.assertEqual(rect1.y, lstOut[0].y)

    def test_sameWidth_load_from_file(self):
        """Test JSON loading from a file"""
        rect1 = Rectangle(10, 7, 2, 8)
        rectLst = [rect1]
        Rectangle.save_to_file(rectLst)
        lstOut = Rectangle.load_from_file()
        self.assertEqual(rect1.width, lstOut[0].width)

    def test_display_method_rec(self):
        """Test display method"""
        disOut = StringIO()
        sys.stdout = disOut
        rec5 = Rectangle(10, 4)
        rec5.display()
        sys.stdout = sys.__stdout__
        theOut = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(disOut.getvalue(), theOut)

    def test_save_to_file_method(self):
        """Test save_to_file method"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        rec11 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([rec11])

        with open("Rectangle.json", "r") as recfile:
            recdata = recfile.read()
        recLst = [{"x": 0, "y": 0, "id": 346, "height": 10, "width": 5}]
        self.assertEqual(recLst, json.loads(recdata))

    def test_err_save_to_file(self):
        """Testing type error"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(self)

    def test_none_save_to_file(self):
        """Checking empty list saved if method failed"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        rect1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as afile:
            dta = afile.read()
        self.assertEqual("[]", dta)

    def test_empty_save_to_file(self):
        """Checking empty list saved if method failed"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        rect1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as afile:
            dta = afile.read()
        self.assertEqual("[]", dta)

    def test_rectangle_to_dictionary(self):
        """Test to_dictionary method"""
        rect15 = Rectangle(12, 9)
        self.assertEqual(type(rect15.to_dictionary()), dict)

    def test_to_dict_print(self):
        """Test type of the dictionary"""
        rect55 = Rectangle(7, 19, 10, 20, 6)
        re55Dict = rect55.to_dictionary()
        ans = {'height': 19, 'id': 6, 'width': 7, 'x': 10, 'y': 20}
        self.assertEqual(re55Dict, ans)

    def test_display_without_y(self):
        rec4 = Rectangle(3, 2, 1)
        r_displ = TestRectangleDisplay.rectangle_stdout(rec4, "display")
        self.assertEqual(" ###\n ###\n", r_displ.getvalue())

    def test_display_all_attributes(self):
        rr = Rectangle(2, 4, 3, 2, 0)
        disp = TestRectangleDisplay.rectangle_stdout(rr, "display")
        rr_display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(rr_display, disp.getvalue())

    def test_display_with_y(self):
        ry = Rectangle(4, 5, 0, 1, 0)
        ryDisp = TestRectangleDisplay.rectangle_stdout(ry, "display")
        displ = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(displ, ryDisp.getvalue())

    def test_err_display(self):
        r_err = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r_err.display(23)


class TestRectangleDisplay(unittest.TestCase):
    """Class to test rectangle's display method"""

    @staticmethod
    def rectangle_stdout(rec, func):
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

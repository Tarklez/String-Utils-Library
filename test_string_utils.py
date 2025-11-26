# test_string_utils.py

import unittest
from string_utils import *

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("123"), "321")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("hello world"), "Hello world")
        self.assertEqual(capitalize_string(""), "")
        self.assertEqual(capitalize_string("Hello"), "Hello")

    def test_strip_string(self):
        self.assertEqual(strip_string("  hello  "), "hello")
        self.assertEqual(strip_string("hello"), "hello")
        self.assertEqual(strip_string("  "), "")
        self.assertEqual(strip_string("  test  case  "), "test  case")

    def test_count_chars(self):
        self.assertEqual(count_chars("hello", "l"), 2)
        self.assertEqual(count_chars("hello", "x"), 0)
        self.assertEqual(count_chars("", "a"), 0)
        self.assertEqual(count_chars("aaa", "a"), 3)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome(""))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("  radar  "))

    def test_replace_char(self):
        self.assertEqual(replace_char("hello", "l", "x"), "hexxo")
        self.assertEqual(replace_char("hello", "z", "x"), "hello")
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_to_lower_case(self):
        self.assertEqual(to_lower_case("Hello"), "hello")
        self.assertEqual(to_lower_case("HELLO"), "hello")
        self.assertEqual(to_lower_case("123"), "123")
        self.assertEqual(to_lower_case(""), "")

    def test_to_upper_case(self):
        self.assertEqual(to_upper_case("hello"), "HELLO")
        self.assertEqual(to_upper_case("Hello"), "HELLO")
        self.assertEqual(to_upper_case("123"), "123")
        self.assertEqual(to_upper_case(""), "")

    def test_split_string(self):
        self.assertEqual(split_string("a,b,c", ","), ["a", "b", "c"])
        self.assertEqual(split_string("hello world"), ["hello", "world"])
        self.assertEqual(split_string(""), [""])
        self.assertEqual(split_string("test"), ["test"])

if __name__ == "__main__":
    unittest.main()
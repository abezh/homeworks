import unittest
from main import reverse_string, is_palindrome, capitalize_words, celsius_to_fahrenheit, fahrenheit_to_celsius

class TestMain(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("how are you?"), "?uoy era woh")
        self.assertNotEqual(reverse_string("Hi"), "hello")
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("12121"))
        self.assertFalse(is_palindrome("swim"))
    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertNotEqual(capitalize_words("hi"), "HI")

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertNotEqual(celsius_to_fahrenheit(1), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertNotEqual(fahrenheit_to_celsius(32), 1)
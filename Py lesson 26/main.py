def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())



def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


import unittest


def reverse(string):
    '''Accepts a string and returns a new string that is its reverse.'''
    assert type(string) == str
    chars = []
    for char in string:
        chars.insert(0, char)
    return ''.join(chars)

import unittest


def reverse(string):
    '''Accepts a string and returns a new string that is its reverse.'''
    assert type(string) == str
    chars = []
    for char in string:
        chars.insert(0, char)
    return ''.join(chars)


class TestReverse(unittest.TestCase):

    def test_raises_assertionerror_if_parameter_is_not_string(self):
        with self.assertRaises(AssertionError):
            reverse(['string'])

    def test_any_string(self):
        new_string = reverse('foo')
        expected = 'oof'
        self.assertEqual(new_string, expected)

    def test_reverses_a_sentence_with_punctuation(self):
        sentence = 'Racecars are the best, you know!'
        reversed_sentence = reverse(sentence)
        expected = '!wonk uoy ,tseb eht era sracecaR'
        self.assertEqual(reversed_sentence, expected)


if __name__ == '__main__':
    unittest.main()

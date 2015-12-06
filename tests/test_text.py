import unittest

from lib.text import Text

class TestPigLatin(unittest.TestCase):
    def setUp(self):
        self.translator = Text()
    
    def test_appends_ay_to_words_starting_with_vowels(self):
        translation = self.translator.pig_latinate('arrow')
        expected = 'arrowyay'
        self.assertEqual(expected, translation)

    def test_appends_starting_consonant_to_end_with_ay(self):
        translation = self.translator.pig_latinate('satin')
        expected = 'atinsay'
        self.assertEqual(expected, translation)

    def test_moves_consonant_cluster_to_the_end(self):
        translation = self.translator.pig_latinate('glove')
        expected = 'oveglay'
        self.assertEqual(expected, translation)
    
    def test_positions_punctuation_correctly(self):
        translation = self.translator.pig_latinate('foo, bar baz: hippo?!')
        expected = 'oofay, arbay azbay: ippohay?!'
        self.assertEqual(expected, translation)


class TestReverse(unittest.TestCase):
    def setUp(self):
        self.text_fun = Text()

    def test_raises_assertionerror_if_parameter_is_not_string(self):
        with self.assertRaises(AssertionError):
            self.text_fun.reverse(['string'])

    def test_any_string(self):
        new_string = self.text_fun.reverse('foo')
        expected = 'oof'
        self.assertEqual(new_string, expected)

    def test_reverses_a_sentence_with_punctuation(self):
        sentence = 'Racecars are the best, you know!'
        reversed_sentence = self.text_fun.reverse(sentence)
        expected = '!wonk uoy ,tseb eht era sracecaR'
        self.assertEqual(reversed_sentence, expected)


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.text_fun = Text()
        self.resp = self.text_fun.fizz_buzz_to_one_hundred()

    def test_returns_fizz_for_multiple_of_three(self):
        mults_of_3 = [i for i in range(1, 101) if i % 3 == 0]
        self.assertTrue(all(['Fizz' in self.resp[i-1] for i in mults_of_3]))

    def test_returns_buzz_for_multiples_of_five(self):
        mults_of_5 = [i for i in range(1, 101) if i % 5 == 0]
        self.assertTrue(all(['Buzz' in self.resp[i-1] for i in mults_of_5]))

    def test_returns_fizzbuzz_for_multiples_of_three_and_five(self):
        mults_15 = [i for i in range(1, 101) if i % 15 == 0]
        self.assertTrue(all(['FizzBuzz' == self.resp[i-1] for i in mults_15]))

    def test_returns_number_for_nonmultiples_of_three_or_five(self):
        nonmultiples = [i for i in self.resp if type(i) == int]
        self.assertTrue(all([i % 3 != 0 and i % 5 != 0 for i in nonmultiples]))


class TestVowelCounter(unittest.TestCase):
    def setUp(self):
        self.text_fun = Text()

    def test_vowel_count_must_take_a_string(self):
        with self.assertRaises(AssertionError) as e:
            self.text_fun.vowel_count(42)
        expected = 'Sentence argument must be a string.'
        self.assertEqual(e.exception.msg, expected)

    def test_vowel_count_returns_dict_of_vowels_and_their_counts(self):
        v_count = self.text_fun.vowel_count('This is my sentence.')
        expected = {'i': 2, 'e': 3, 'y': 1}
        self.assertEqual(v_count, expected)

    def test_y_is_vowel_returns_false_for_beginning_y_by_a_vowel(self):
        resp = self.text_fun.y_is_vowel('yellow', 0)
        self.assertEqual(resp, False)

    def test_y_is_vowel_returns_true_for_beginning_y_by_a_consonant(self):
        resp = self.text_fun.y_is_vowel('Ydris', 0)
        self.assertEqual(resp, True)


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.text_fun = Text()

    def test_returns_False_if_not_palindrome(self):
        resp = self.text_fun.is_palindrome('greg')
        self.assertEqual(resp, False)

    def test_returns_True_if_palindrom(self):
        resp = self.text_fun.is_palindrome('racecar')
        self.assertEqual(resp, True)

    def test_normalizes_case(self):
        resp = self.text_fun.is_palindrome('Racecar')
        self.assertEqual(resp, True)

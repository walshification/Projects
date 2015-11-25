import unittest
from projects.pig_latin import PigLatin
from projects.reverse_a_string import reverse
from projects.fizz_buzz import fizz_buzz_to_one_hundred

class TestPigLatin(unittest.TestCase):

    def setUp(self):
        self.translator = PigLatin()
    
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
        translation = self.translator.pig_latinate('foo, bar baz: purple hippo?!')
        expected = 'oofay, arbay azbay: urplepay ippohay?!'
        self.assertEqual(expected, translation)


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


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.resp = fizz_buzz_to_one_hundred()

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

import unittest
from projects.pig_latin import PigLatin
from projects.reverse_a_string import reverse


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

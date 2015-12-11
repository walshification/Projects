import unittest
from collections import defaultdict

from lib.text import Text, Word, TextCounter


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
    def test_any_string(self):
        new_string = Word('foo').reverse()
        expected = 'oof'
        self.assertEqual(new_string, expected)

    def test_reverses_a_sentence_with_punctuation(self):
        sentence = 'Racecars are the best, you know!'
        reversed_sentence = Word(sentence).reverse()
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
    def test_returns_defaultdict_of_vowels_and_their_counts(self):
        v_count = TextCounter('sentence').vowels
        expected = defaultdict(int, {'e': 3})
        self.assertEqual(v_count, expected)

    def test_ignores_y_when_it_is_a_consonant(self):
        v_count = TextCounter('yellow').vowels
        expected = defaultdict(int, {'e': 1, 'o': 1})
        self.assertEqual(v_count, expected)

    def test_includes_beginning_y_when_followed_by_a_consonant(self):
        v_count = TextCounter('Ydris').vowels
        expected = defaultdict(int, {'y': 1, 'i': 1})
        self.assertEqual(v_count, expected)

    def test_y_is_vowel_returns_true_for_nonbeginning_y_letters(self):
        v_count = TextCounter('dry').vowels
        expected = defaultdict(int, {'y': 1})
        self.assertEqual(v_count, expected)


class TestPalindrome(unittest.TestCase):
    def test_returns_False_if_not_palindrome(self):
        word = Word('greg')
        resp = word.is_palindrome()
        self.assertEqual(resp, False)

    def test_returns_True_if_palindrom(self):
        word = Word('racecar')
        resp = word.is_palindrome()
        self.assertEqual(resp, True)

    def test_normalizes_case(self):
        word = Word('Racecar')
        resp = word.is_palindrome()
        self.assertEqual(resp, True)


class TestTextCounter(unittest.TestCase):
    def setUp(self):
        self.tc = TextCounter('This is a sample. Yep! Ygritte\'s still sad.')

    def test_returns_word_count_in_string(self):
        self.assertEqual(self.tc.word_count, 8)

    def test_most_common_returns_tuple_of_most_common_char_and_count(self):
        self.assertTrue(self.tc.most_common, ('s', 4))

    def test_most_common_returns_tuple_list_if_more_than_one_most_common(self):
        self.tc = TextCounter('Hit list')
        expected = [('i', 2), ('t', 2)]
        self.assertTrue(all(c in self.tc.most_common for c in expected))

    def test_reads_words_from_a_file(self):
        tc_from_f = TextCounter(file_path='tests/fixtures/text.txt')
        expected = ['This', 'was', 'successful\n']
        self.assertEqual(tc_from_f.words, expected)

    def test_raises_ArgumentError_if_no_text_souce_give(self):
        with self.assertRaises(AssertionError):
            TextCounter()

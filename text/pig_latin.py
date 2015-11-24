import string
import unittest


def pig_latinate(sentence):
    '''Translates a string from English into Pig Latin.'''
    assert type(sentence) is str, "{} is not a string.".format(sentence)
    p_lat_list = []
    for word in sentence.split():
        word, punctuation = splunc(word)
        if word[0] in 'aeiou':
            word += 'y'
        else:
            word = postpend_cons(word)
        p_lat_list.append('{}ay{}'.format(word, punctuation))
    return ' '.join(p_lat_list)


def postpend_cons(word):
    '''Moves the first consonants of a word to the end of the word.'''
    first_consonants = ''
    for char in word:
        if char not in 'aeiou':
            first_consonants += char
        else:
            break
    return word[len(first_consonants):] + first_consonants


def splunc(word):
    '''
    Takes in a string and returns a tuple of the word split from its punctuation.
    Returns the word and an empty string if no punctuation is present.
    '''
    puncs, letters = [], []
    [puncs.insert(0, char) if char in string.punctuation else letters.insert(0, char)
     for char in word[::-1]]
    return (''.join(letters), ''.join(puncs))


class TestPigLatin(unittest.TestCase):
    
    def test_appends_ay_to_words_starting_with_vowels(self):
        translation = pig_latinate('arrow')
        expected = 'arrowyay'
        self.assertEqual(expected, translation)

    def test_appends_starting_consonant_to_end_with_ay(self):
        translation = pig_latinate('satin')
        expected = 'atinsay'
        self.assertEqual(expected, translation)

    def test_moves_consonant_cluster_to_the_end(self):
        translation = pig_latinate('glove')
        expected = 'oveglay'
        self.assertEqual(expected, translation)
    
    def test_positions_punctuation_correctly(self):
        translation = pig_latinate('foo, bar baz: purple hippo?!')
        expected = 'oofay, arbay azbay: urplepay ippohay?!'
        self.assertEqual(expected, translation)


if __name__ == '__main__':
    unittest.main()

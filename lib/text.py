import string
from collections import defaultdict


class Text(object):
    def __init__(self):
        self.vowels = 'aeiou'
        self.consonants = 'bcdfghjklmnpqrstvwxz'  # does not include 'y'

    def fizz_buzz_to_one_hundred(self):
        """Prints numbers 1 to 100, but prints "Fizz" instead of the
        number for multiples of three, "Buzz" for multiples of five, and
        "FizzBuzz" for multiples of both three and five.
        """
        numbers = []
        for i in range(1, 101):
            numbers.append('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
        return numbers
    
    def pig_latinate(self, sentence):
        """Translates a string from English into Pig Latin."""
        assert type(sentence) is str, "{} is not a string.".format(sentence)
        p_lat_list = []
        for word in sentence.split():
            word, punctuation = self.splunctuate(word)
            if word[0] in 'aeiou':
                word += 'y'
            else:
                word = self.postpend_cons(word)
            p_lat_list.append('{}ay{}'.format(word, punctuation))
        return ' '.join(p_lat_list)
    
    
    def postpend_cons(self, word):
        """Moves the first consonants of word to the end of the word."""
        first_consonants = ''
        for char in word:
            if char not in 'aeiou':
                first_consonants += char
            else:
                break
        return word[len(first_consonants):] + first_consonants
    
    
    def splunctuate(self, word):
        """Takes in a string and returns a tuple of the word split from
        its punctuation. Returns the word and an empty string if no
        punctuation is present.
        """
        puncs, letters = [], []
        for char in word[::-1]:
            if char in string.punctuation:
                puncs.insert(0, char)
            else:
                letters.insert(0, char)
        return (''.join(letters), ''.join(puncs))


class Word(str):
    def __new__(cls, content):
        return super().__new__(cls, content)

    def is_palindrome(self):
        """Returns Boolean if word is palindrome."""
        word = self.lower()
        if word == None or len(word) == 1:
            return True
        return Word(word[1:-1]).is_palindrome() if word[0] == word[-1] else False

    def count_vowels(self):
        """Returns a dict with the word's vowels as keys and count as
        values.
        """
        word = Word(self.lower())
        count = defaultdict(int)
        for char in word:
            if word.is_vowel(char, word.index(char)):
                count[char] += 1
        return count

    def is_vowel(self, char, char_index):
        """Returns Boolean if the character in a word is a vowel or
        not.
        """
        if char in 'aeiou':
            return True
        elif char == 'y' and (char_index > 0 or self[1] not in 'aeiou'):
            return True
        else:
            return False

    def reverse(self):
        """Returns a copy of a string in reverse."""
        return Word(self[::-1])

import string


class Text(object):
    def __init__(self):
        self.vowels = 'aeiou'

    def fizz_buzz_to_one_hundred(self):
        """Prints numbers 1 to 100, but prints "Fizz" instead of the
        number for multiples of three, "Buzz" for multiples of five, and
        "FizzBuzz" for multiples of both three and five.
        """
        numbers = []
        for i in range(1, 101):
            numbers.append('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
        return numbers

    def reverse(self, string):
        """Accepts a string and returns its reverse."""
        assert type(string) == str
        chars = []
        for char in string:
            chars.insert(0, char)
        return ''.join(chars)
    
    def pig_latinate(self, sentence):
        """Translates a string from English into Pig Latin."""
        assert type(sentence) is str, "{} is not a string.".format(sentence)
        p_lat_list = []
        for word in sentence.split():
            word, punctuation = self.splunc(word)
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
    
    
    def splunc(self, word):
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

    def vowel_count(self, sentence):
        """Takes a string and returns a dict with with the string's
        vowels as keys and their count as values.
        """
        assert type(sentence) == str, 'Sentence argument must be a string.'
        words = sentence.split(' ')
        count = {}
        for word in words:
            for char in word:
                if char in self.vowels:
                    count[char] = (count.get(char) or 0) + 1
                elif char == 'y' and self.y_is_vowel(word, word.index(char)):
                    count[char] = (count.get(char) or 0) + 1
        return count

    def y_is_vowel(self, word, y_index):
        """Returns Boolean if 'y' is used as a vowel or not."""
        assert type(word) == str, 'Word argument must be a string.'
        if y_index > 0:
            return True
        else:
            if word[1] in self.vowels:
                return False
            else:
                return True

    def is_palindrome(self, word):
        """Returns True or False if word is palindrome or not."""
        assert type(word) == str, 'Word must be a string.'
        if word == None or len(word) == 1: return True
        word = word.lower()
        return self.is_palindrome(word[1:-1]) if word[0] == word[-1] else False

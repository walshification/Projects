import string


class Text(object):
    def fizz_buzz_to_one_hundred(self):
        '''
        Prints the numbers from 1 to 100, but prints "Fizz" instead of the
        number for multiples of three, "Buzz" for multiples of five, and "FizzBuzz"
        for multiples of both three and five.
        '''
        numbers = []
        for i in range(1, 101):
            numbers.append('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
        return numbers

    def reverse(self, string):
        '''Accepts a string and returns a new string that is its reverse.'''
        assert type(string) == str
        chars = []
        for char in string:
            chars.insert(0, char)
        return ''.join(chars)
    
    def pig_latinate(self, sentence):
        '''Translates a string from English into Pig Latin.'''
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
        '''Moves the first consonants of a word to the end of the word.'''
        first_consonants = ''
        for char in word:
            if char not in 'aeiou':
                first_consonants += char
            else:
                break
        return word[len(first_consonants):] + first_consonants
    
    
    def splunc(self, word):
        '''
        Takes in a string and returns a tuple of the word split from its punctuation.
        Returns the word and an empty string if no punctuation is present.
        '''
        puncs, letters = [], []
        [puncs.insert(0, char) if char in string.punctuation else letters.insert(0, char)
         for char in word[::-1]]
        return (''.join(letters), ''.join(puncs))

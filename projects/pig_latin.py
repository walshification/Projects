import string


class PigLatin(object):
    
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

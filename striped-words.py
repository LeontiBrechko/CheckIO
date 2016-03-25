VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

import re

def checkio(text):
    words = re.findall(r'\b([A-Z][A-Z]+)\b', text.upper())
    def striped_word(word):
        for i in range(len(word) - 1):
            if (word[i] in VOWELS and word[i + 1] in VOWELS) or (word[i] in CONSONANTS and word[i + 1] in CONSONANTS):
                return False
        return True
    return len(filter(striped_word, words))
'''
def checkio(text):
    text = text.upper()
    for c in PUNCTUATION:
        text = text.replace( c, " " )
    for c in VOWELS:
        text = text.replace( c, "v" )
    for c in CONSONANTS:
        text = text.replace( c, "c" )
    words = text.split( " " )
    count = 0
    for word in words:
        if len( word ) > 1 and word.isalpha():
            if word.find( "cc" ) == -1 and word.find( "vv" ) == -1:
                count += 1
    return count
'''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

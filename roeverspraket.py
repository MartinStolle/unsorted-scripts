# -*- coding: utf-8 -*-
'''Implementation of JSONDecoder

[2015-04-27] Challenge #212 [Easy] Rövarspråket

You take an ordinary word and replace the consonants
with the consonant doubled and with an "o" in between.

So the consonant "b" is replaced by "bob", "r" is
replaced with "ror", "s" is replaced with "sos".

Vowels are left intact.
'''
import re

vowels = ('a', 'e', 'i', 'o', 'u', 'å', 'ä', 'ö')
alphanumeric = re.compile(r'\w')


def encode(text):
    '''Decoding the text and convert it into Rövarspråket

    >>> encode("Jag talar Rövarspråket!")
    'Jojagog totalolaror Rorövovarorsospoproråkoketot!'
    >>> encode("I'm speaking Robber's language!")
    "I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!"
    >>> encode("Tre Kronor är världens bästa ishockeylag.")
    'Totrore Kokrorononoror äror vovärorloldodenonsos bobäsostota isoshohocockokeyoylolagog.'
    >>> encode("Vår kung är coolare än er kung.")
    'Vovåror kokunongog äror cocoololarore änon eror kokunongog.'
    '''
    encoded = []
    for letter in text:
        if alphanumeric.match(letter)and letter.lower() not in vowels:
            encoded.append(letter)
            encoded.append('o')
            encoded.append(letter.lower())
        else:
            encoded.append(letter)
    return ''.join(encoded)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

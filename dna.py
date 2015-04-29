# -*- coding: utf-8 -*-
'''Implementation of the challenge

[2015-03-23] Challenge #207 [Easy] Bioinformatics 1: DNA Replication

DNA - deoxyribonucleic acid - is the building block of every organism.
It contains information about hair color, skin tone, allergies, and more.
It's usually visualized as a long double helix of base pairs.
DNA is composed of four bases - adenine, thymine, cytosine, guanine;
paired as follows: A-T and G-C.
'''
pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def complementary_strand(strand):
    '''It is your job to generate one side of the DNA strand and output
    the two DNA strands. Your program should take a DNA sequence as
    input and return the complementary strand.

    >>> complementary_strand('A A T G C C T A T G G C')
    'A A T G C C T A T G G C\\nT T A C G G A T A C C G'
    '''
    return '{0}\n{1}'.format(
        strand, ' '.join([pairs[x] for x in strand if x in pairs])
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()

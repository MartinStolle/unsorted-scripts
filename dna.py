# -*- coding: utf-8 -*-
'''Implementation of the challenge

[2015-03-23] Challenge #207 [Easy] Bioinformatics 1: DNA Replication

DNA - deoxyribonucleic acid - is the building block of every organism.
It contains information about hair color, skin tone, allergies, and more.
It's usually visualized as a long double helix of base pairs.
DNA is composed of four bases - adenine, thymine, cytosine, guanine;
paired as follows: A-T and G-C.
'''
PAIRS = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

CODONS = {
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Asn': ['AAT', 'AAC'],
    'Asp': ['GAT', 'GAC'],
    'Cys': ['TGT', 'TGC'],
    'Gln': ['CAA', 'CAG'],
    'Glu': ['GAA', 'GAG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'His': ['CAT', 'CAC'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Lys': ['AAA', 'AAG'],
    'Met': ['ATG'],
    'Phe': ['TTT', 'TTC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'STOP': ['TAA', 'TAG', 'TGA'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Trp': ['TGG'],
    'Tyr': ['TAT', 'TAC'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
}
PAIRSCODONS = dict((pair, codon) for codon, pairs in CODONS.items()
                   for pair in pairs)


def complementary_strand(strand):
    '''It is your job to generate one side of the DNA strand and output
    the two DNA strands. Your program should take a DNA sequence as
    input and return the complementary strand.

    >>> complementary_strand('A A T G C C T A T G G C')
    'A A T G C C T A T G G C\\nT T A C G G A T A C C G'
    '''
    return '{0}\n{1}'.format(
        strand, ' '.join([PAIRS[x] for x in strand if x in PAIRS])
    )


def translated_protein_sequence(sequence):
    '''Take a DNA sequence and emit the translated protein sequence.
    Every generated DNA strand starts with a Met codon and ends with
    a STOP codon.

    >>> translated_protein_sequence('A T G T T T C G A G G C T A A')
    'Met Phe Arg Gly STOP'
    '''
    proteinSequence = []
    sequence = sequence.replace(' ', '')  # remove whitespace
    for basepair in [sequence[i:i+3] for i in range(0, len(sequence), 3)]:
        proteinSequence.append(PAIRSCODONS[basepair])
    return ' '.join(proteinSequence)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

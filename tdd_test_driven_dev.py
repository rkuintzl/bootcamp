import pytest
import bioinfo_dicts

def n_neg(seq):
    """Number of negative residues in a protein sequence."""

    seq = seq.upper()

    # Check for sequence validity
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + 'is not a valid amino acid.')

    # Count GLUs (E) and ASPs (D) and return count
    return seq.count('D') + seq.count('E')
    return None

def find_codon_lesson6(codon, mrna_seq, protein_seq):
    """Find a specified, in-frame codon with a given mRNA sequence;
       the encoded aa must also be found in the protein_seq."""

    mrna_seq = mrna_seq.upper().replace('U', 'T')
    check_codon(codon)
    check_protein_valid(protein_seq)
    check_mrna_valid(mrna_seq)

    i = 0
    # Scan sequence until we hit the specified codon or the end of the sequence
    while i+2 < len(mrna_seq): #check
        if mrna_seq[i:i+3] == codon:
            aa = bioinfo_dicts.codons[codon]
            if aa in protein_seq:
                return i
        i += 1

    return -1

def check_codon(codon):
    if len(codon) != 3:
        raise RuntimeError("Your codon must be three nucleotides long.")
    for base in codon:
        if not base in bioinfo_dicts.bases:
            raise RuntimeError(base + 'in codon is not a valid nucleotide.')

def check_protein_valid(seq):
    for aa in seq:
        if not aa in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + 'is not a valid amino acid.')

def check_mrna_valid(seq):
    for base in seq:
        if not base in bioinfo_dicts.bases:
            raise RuntimeError(base + 'is not a valid nucleotide.')


def ratio(x,y):
    """The ratio of 'x' to 'y'."""
    return x / y

def complement_base(base, material='DNA'): # This specifies the default value as DNA
    """Return the Watson-Crick complement of a base"""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid material.')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    else:
        raise RuntimeError('Invalid material.')

def reverse_complement(seq,material='DNA'):
    """Compute reverse complement of a DNA sequence"""

    # Initialize empty string
    revComp = ''

    revSeq = seq[::-1]

    # Loop through and add new rev comp bases

    #for base in revsersed(seq):
    for base in revSeq:
        revComp += complement_base(base,material=material)

    return revComp


def reverse_complement2(seq,material='DNA'):
    """Compute reverse complement of a DNA sequence without loops"""

    # Reverse the sequence:
    revSeq = seq[::-1]
    revSeq = revSeq.upper()

    # Make all DNA regardless of material:
    revComp = revSeq.replace('U','T')

    # Alias A and C:
    revComp = revComp.replace('A','B')
    revComp = revComp.replace('C','D')

    # Complement T and G:
    revComp = revComp.replace('T','A')
    revComp = revComp.replace('G','C')

    # Complement aliased A and C:
    revComp = revComp.replace('D','G')
    if material == 'DNA':
        revComp = revComp.replace('B','T')
    elif material == 'RNA':
        revComp = revComp.replace('B','U')



#    i = 0
 #   while i < len(revSeq):
  #      base = revSeq[i]
   #     revComp += complement_base(base,material=material)
    #    i += 1

    return revComp




"""bootcamp_utils: A collection of statistical functions
proved useful to 55 students."""

import numpy as np

def ecdf(data):
    """
    Compute x, y values for an empirical cumulative distribution function.
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

def read_fasta(fasta_file):
    """Given the filename for a fasta file,
    returns a dictionary mapping defline IDs to sequence objects.
    Also cleans up sequences by forcing all caps."""

    seq_dict = dict() # Declare a new dictionary

    with open(fasta_file,'r') as f:
        lines = f.readlines()
        defline = ""
        for li in lines:
            li = li.rstrip() # remove newlines
            if '>' in li:
                defline = li.replace('>','') # if i use 'id' it is blue; why?
                seq_dict[defline] = ""
            else:
                li = li.upper() # just to clean up sequence
                seq_dict[defline] += li

    return seq_dict

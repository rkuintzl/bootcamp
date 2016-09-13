import sys
import bioinfo_dicts


def find_longest_orfs(seq,n_orfs):
    """Finds all longest ORFs in provided sequence, and returns 'n' of them."""

    # Make sure there is a start codon in the sequence:
    if not 'ATG' in seq:
        raise RuntimeError("Your DNA sequence doesn't have a start codon.")

    # Initialize orfs list:
    orfs =[]

    # Loop over sequence and find ORFs:
    for i, base in enumerate(seq):
        triplet = seq[i:i+3]
        if triplet == 'ATG':
            orf_seq = ''
            aa_seq = ''
            j = i
            while j+2 < len(seq):
                codon = seq[j:j+3]
                orf_seq += codon
                if bioinfo_dicts.codons[codon] == '*': # if stop codon
                    orf_len = len(orf_seq)
                    orfs.append((orf_len,orf_seq,aa_seq)) # j is orf len in nts
                    break # this only breaks out of while loop, right?
                else:
                    aa_seq += bioinfo_dicts.codons[codon]
                    j+=3

    # Sort orf list by length
    orfs.sort()

    # Select n longest orfs to return:
    number = -(n_orfs+1)
    longest_orfs = orfs[:number:-1]

    longest_orfs = tuple(longest_orfs)
    return longest_orfs

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
                defline = li # if i use 'id' it is blue; why?
                seq_dict[defline] = ""
            else:
                li = li.upper() # just to clean up sequence
                seq_dict[defline] += li

    return seq_dict

#############################################
## Begin "executable" portion of code here ##
#############################################

print("Usage: <fasta file> <number of long ORFs to find (integer)> <print 'aa' sequence or 'nt'>")

fasta = sys.argv[1]
n_orfs = int(sys.argv[2])
seq_type = sys.argv[3]

seq_dict = read_fasta(fasta)

for defline in seq_dict.keys():
    seq = seq_dict[defline]
    orfs = find_longest_orfs(seq,n_orfs)
    for orf in orfs:
        (orf_len,orf_seq,aa_seq) = orf
        defline_new = defline + " LENGTH=" + str(orf_len)
        if seq_type == 'aa':
            print(defline_new + "\n" + aa_seq)
        elif seq_type == 'nt':
            print(defline_new + "\n" + orf_seq)
        else:
            raise RuntimeError(seq_type + "is not a permitted sequence type.")

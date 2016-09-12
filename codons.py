
codon = input('Input your codon here: ') # Note: this is no longer "raw_input" in python 3

codon_list = ('UAA','UAG','UGA')

if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_list:
    print('This is a stop codon.')
else:
    print('This is neither a start nor a stop codon.')

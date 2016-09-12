
def parensAreGood(structure):
    """Makes sure that the number of left parens equals the number of right parens"""
    leftCount = structure.count('(')
    rightCount = structure.count(')')
    if leftCount == rightCount:
        return True
    else:
        return False


def dotparen_to_bp(structure):
    """Converts dot-parens notation to a tuple of 2-tuples representing base pairs"""
    # Initialize empty tuples:
    parenList = []
    tempList = []

    for i, _ in enumerate(structure):
        if '(' == structure[i]:
            tempList.append((i,'left'))
        elif ')' == structure[i]:
            tempList.append((i,'right'))

    tempList.sort() # This sorts properly on first term of inner list

    hairpinList = []
    single_hairpin = []
    hairpinFound = 0
    endOfLastHairpin = 0

    for i, paren in enumerate(tempList):
        (index,side) = paren
        if side == 'right':
            if i+1 < len(tempList):
                nextparen = tempList[i+1][1]
                if nextparen == 'left':
                    single_hairpin = tempList[endOfLastHairpin:i+1]
                    endOfLastHairpin = i+1
                    hairpinFound = 1
            else:
                single_hairpin = tempList[endOfLastHairpin:i+1]
                endOfLastHairpin = i+1
                hairpinFound = 1

        if hairpinFound == 1:
            print("Hairpin found!")
            hairpinList.append(single_hairpin)
            # Reset hairpin
            hairpinFound = 0
            single_hairpin = []

    # At this point, you should have a list of several hairpins,
    # each of which has several positions and should have equal number of
    # left and right parens and are sorted properly. But let's double-check:

    for hairpin in hairpinList:
        left_list = []
        right_list = []
        for paren in hairpin:
            (index,side) = paren
            if side == 'left':
                left_list.append(index)
            elif side == 'right':
                right_list.append(index)
        if len(right_list) == len(left_list):
            for left_index in left_list:
                right_index = right_list.pop()
                parenList.append((left_index,right_index))
        else:
            raise RuntimeError('Invalid hairpin!')

    parenTuple = tuple(parenList)
    print (parenTuple)
    return parenTuple

def stericallySound(structure):
    """Ensures that the RNA structure is sterically sound"""
    if '(..)' in structure or '(.)' in structure or '()' in structure:
        return False
    else:
        return True

def rna_ss_validator(seq, ss_tuple, wobble=True):
    """Check whether secondary structure prediction is valid"""
    for i, pair in enumerate(ss_tuple):
        (first,second) = pair # first and second are indeces
        base1 = seq[first]
        base2 = seq[second]
        print(base1,base2)
        if not (paired(base1,base2) or (wobblePaired(base1,base2) and wobble==True)):
            return False
    return True

def paired(base1,base2):
    """Checks for valid Watson-Crick pair"""
    if 'G' in base1 and 'C' in base2:
        return True
    elif 'C' in base1 and 'G' in base2:
        return True
    elif 'A' in base1 and 'U' in base2:
        return True
    elif 'U' in base1 and 'A' in base2:
        return True
    else:
        return False

def wobblePaired(base1,base2):
    """Checks for valid G-U wobble pair"""
    if 'G' in base1 and'U' in base2:
        return True
    elif 'U' in base1 and 'G' in base2:
        return True
    else:
        return False

### Execute code ###

# Note: add function to make sure len(structure) == len(seq)
seq = 'AGGGGGGGCCTGGGGGCAAAAAGG'
structure = '(((.....)))......(.....))'

# seq = 'AAAGGGGGTTTGGGGGCCCGGGGGGGG'
# structure = '(((.....))).....(((.....)))'
wobble = True

if parensAreGood(seq) and stericallySound(structure):
    ss_tuple = dotparen_to_bp(structure)
    if rna_ss_validator(seq,ss_tuple,wobble=wobble):
        print("Your secondary structure is valid.")
    else:
        print("Your secondary structure is not valid.")

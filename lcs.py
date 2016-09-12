
# Find longest common substring (LCS)

string1 = 'ATGCATAT'
string2 = 'GCATCCCA'

def getSubstrings(string):
    """Store all possible substrings of input sequence"""
    list = []
    for i, _ in enumerate(string):
        for j in range(i,len(string)):
            print(i,j)
            substr = string[i:j]
            list.append(substr)
    return list

def findLCS(substrings_list,string2):
    """Find Largest Common Substring"""
    LCS = ''
    maxLCS = 0
    for substr in substrings_list:
        if substr in string2 and len(substr) > maxLCS:
            LCS = substr
            maxLCS = len(substr)
    return LCS

# Retrieve substrings of first sequence (eventually make this the shortest sequence):
substrings_list = getSubstrings(string1)
LCS = findLCS(substrings_list,string2)
print(LCS)

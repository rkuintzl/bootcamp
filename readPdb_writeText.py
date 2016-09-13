with open('data/1OLG.pdb','r') as f, open('atoms_chain_A.txt','w') as f_out:

    # Get all the lines

    lines = f.readlines()

    #

    # Put the ATOM lines from chain A in a new file

    for li in lines:

        # if wanted to strip newlines:
        li = li.rstrip()

        if len(li) > 21 and li[:4] == 'ATOM' and li[21] == 'A':

            f_out.write(li)

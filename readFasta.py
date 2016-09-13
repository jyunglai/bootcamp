import os

#Read single fasta file and store as one strings
with open('EcMscS.fasta', 'r') as f, open('singleStringFasta.txt', 'w') as f_out:
    #Get all lines
    lines = f.readlines()
    seq = ''

    for line in lines:
        print(line.find('>'))
        if line.find('>') == 0:
            pass
        else:
            seq += line.rstrip()

    f_out.write(seq)

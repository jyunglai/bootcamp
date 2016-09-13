import os

f = open('data/1OLG.pdb', 'r')

type(f)

f_str = f.read()

print(f_str[:1000])

#Returns to the beginning of the i/o stream
f.seek(0)

#Read contents of the file in as a list
f_list = f.readlines()

#print(f_list)

#Tells you whether the file is open for input / output
f.close

#Closes a file
f.close()

#Automatically closing a file after Useful
with open('data/1OLG.pdb', 'r') as f:
    f_lines = f.readlines()
    print('In the with cluase is the file closed?', f.closed)
    print('Out of the with cluase is the file closed?', f.close)


with open('data/1OLG.pdb', 'r') as f:
    counter = 0
    for line in f:
        print(line.rstrip())
        counter += 1
        if counter >= 10:
            break

print('Is file closed', f.closed)

#Another way to read line
with open('data/1OLG.pdb', 'r') as f:
    counter = 0
    while counter < 10:
        print(f.readline().rstrip())
        counter += 1

#Writing to the file
#Checking if file is already in the current directory, before writing to a file
print('Does the file exist?: ', os.path.isfile('data/1OLG.pdb'))

#if os.path.isfile('mastery.txt'):
#    raise RuntimeError('File mastery.txt already exists.')

with open('mastery.txt', 'w') as f:
    f.write('This is my life.\n')
    f.write('There are many like it, but this one is mine.\n')
    f.write('I must master mu file like I must master my life.\n')

#if os.path.isfile('gimme_phi.txt'):
#    raise RuntimeError('File gimme_phi.txt already exists')

with open('gimme_phi.txt', 'w') as f:
    f.write('The golden ratio, phi = ')
    #f.write(1.61803398875) #This is an error, it only writes strings
    f.write('{phi:.8f}'.format(phi = 1.61803398875))

#Use !cat name_of_file to open file outside of ipython in bash

#Exercise
#extract atomic coordinates from a pdb file for the first tetramer
with open('data/1OLG.pdb', 'r') as f, open('atoms_chain_A.txt', 'w') as f_out:
    # Get all the lines
    lines = f.readlines()

    # Put the ATOM lines from chain A in new file
    for line in lines:
        if len(line) > 21 and line[:4] == 'ATOM' and line[21] == 'A':
            f_out.write(line)
#Read out of data... and Write to atoms...
